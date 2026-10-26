"""Public IP information access layer (ipify + ipwho.is).

Everything that talks to the network lives here: fetching the public
IPv4 and IPv6 addresses (ipify), and enriching the IPv4 address with
geolocation, ISP and ASN data (ipwho.is). Every failure is translated
into a plain result dictionary so the rest of the app never has to
handle raw exceptions.

Result shape (matching the option-1 app's convention):
    {"ok": True,  "data": ...}
    {"ok": False, "title": str, "detail": str}
    plus, only for IPv6 when the network simply has none:
    {"ok": False, "unavailable": True, ...}  (shown as info, not error)

REST APIs used (both free):
  * ipify     - https://www.ipify.org/        (public IPv4 / IPv6)
  * ipwho.is  - https://ipwho.is/             (geo, ISP, ASN; no key)

Based on the same REST + JSON concepts as Cisco lab 4.9.2
(DevNet Project Activity 3, Option 2).
"""

import requests

TIMEOUT_SECONDS = 10

IPV4_URL = "https://api.ipify.org?format=json"    # IPv4 only
IPV6_URL = "https://api6.ipify.org?format=json"   # IPv6 only (fails without IPv6)


def _fail(title: str, detail: str) -> dict:
    return {"ok": False, "title": title, "detail": detail}


def _get_json(url: str) -> dict:
    """GET a URL and return parsed JSON, or a failure dictionary.

    Handles the network/HTTP/JSON layers once for all API calls.
    """
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
    except requests.exceptions.ConnectionError:
        return _fail(
            "No network connection",
            "Could not reach the API. Check your internet connection "
            "and try again.")
    except requests.exceptions.Timeout:
        return _fail(
            "The request timed out",
            f"The API did not answer within {TIMEOUT_SECONDS} seconds. "
            "Please try again.")

    if response.status_code in (401, 403):
        return _fail(
            "Invalid or unauthorized API key",
            "The API rejected the key. Check your key at ipify.org and "
            "update config.ini (or the IPIFY_KEY environment variable).")

    try:
        data = response.json()
    except ValueError:
        return _fail(
            "Unexpected response from the API",
            f"HTTP {response.status_code}: the response was not valid "
            "JSON. Please try again.")

    # ipify answers with a 4xx + {"message": ...} body on errors.
    if response.status_code >= 400:
        return _fail("API error", str(data.get("message", data)))
    return data


def _address(url: str, key: str, family: str) -> dict:
    """Fetch one public address from an ipify endpoint."""
    url = f"{url}&apiKey={key}" if key else url
    data = _get_json(url)
    if data.get("ok") is False:
        # A missing IPv6 route is a normal situation, not an error:
        # mark it so main/display can show a friendly info line.
        if family == "ipv6" and "timed out" in data.get("title", "").lower():
            return {"ok": False, "unavailable": True, **data}
        return data
    ip = data.get("ip", "").strip()
    if not ip:
        return _fail(f"No {family} address returned",
                     "The API responded without an address. Try again.")
    return {"ok": True, "ip": ip}


def get_ipv4(key: str) -> dict:
    """Return the computer's public IPv4 address."""
    return _address(IPV4_URL, key, "ipv4")


def get_ipv6(key: str) -> dict:
    """Return the computer's public IPv6 address ('unavailable' if none)."""
    return _address(IPV6_URL, key, "ipv6")


def enrich(ip: str) -> dict:
    """Look up geolocation, ISP and ASN data for an IPv4 address.

    ipwho.is needs no key and answers with fields such as:
    success, ip, type, country, region, city, latitude, longitude,
    connection: {asn, org, isp, domain}, timezone: {id, utc}.
    """
    data = _get_json(f"https://ipwho.is/{ip}")
    if data.get("ok") is False:
        return data
    if not data.get("success", False):
        return _fail(
            "Lookup failed",
            data.get("message") or "ipwho.is could not enrich that "
            "address. The other information is still shown.")
    return {"ok": True, "data": data}
