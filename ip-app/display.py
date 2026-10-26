"""All screen output for the IP address app.

Feature-enhancement layer in the same style as the option-1 app:
the plain print() statements typical of a first REST API program are
replaced with colored, table-formatted output using the rich library,
and every failure is shown as a red panel instead of a traceback.
"""

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_banner() -> None:
    """App title banner shown once at startup."""
    console.print(Panel.fit(
        "[bold cyan]Public IP Address Info[/]\n"
        "[dim]ipify + ipwho.is REST APIs - lab 4.9.2 concepts"
        " - DevNet Project Activity 3, Option 2[/]",
        border_style="cyan",
    ))


def show_error(title: str, detail: str) -> None:
    """Render any failure as a red panel - never a raw traceback."""
    console.print(Panel(
        f"[bold red]{title}[/]\n{detail}",
        border_style="red",
        title="Lookup failed",
    ))


def show_info(title: str, detail: str) -> None:
    """Non-failure notice (e.g. IPv6 not available on this network)."""
    console.print(Panel(
        f"[bold yellow]{title}[/]\n{detail}",
        border_style="yellow",
        title="Notice",
    ))


def show_ip_info(ipv4: dict, ipv6: dict, geo: dict) -> None:
    """Render the combined IP information table.

    ipv4: result of api.get_ipv4();  ipv6: result of api.get_ipv6();
    geo:  result of api.enrich() - any of them may be {"ok": False}.
    """
    if not ipv4.get("ok"):
        show_error(ipv4.get("title", "Unknown error"),
                   ipv4.get("detail", ""))
        return

    info = Table(show_header=False, box=box.ROUNDED, border_style="green",
                 title="[bold green]Your Public IP Information[/]",
                 padding=(0, 2))
    info.add_column(style="bold cyan", justify="right")
    info.add_column()

    # --- Addresses ------------------------------------------------------
    info.add_row("IPv4", ipv4["ip"])
    if ipv6.get("ok"):
        info.add_row("IPv6", ipv6["ip"])
    else:
        info.add_row("IPv6", "[dim]Not available on this network[/]")

    # --- Enrichment (geolocation, ISP, ASN) -----------------------------
    if geo.get("ok"):
        d = geo["data"]
        connection = d.get("connection") or {}
        timezone = d.get("timezone") or {}

        location = ", ".join(str(part) for part in (
            d.get("city"), d.get("region"), d.get("country")) if part)
        if location:
            info.add_row("Location", location)
        if d.get("latitude") is not None:
            coords = f"{d['latitude']:.4f}, {d.get('longitude', 0):.4f}"
            info.add_row("Coordinates", coords)
        if timezone.get("id"):
            utc = f" (UTC {timezone.get('utc', '')})".replace("()", "")
            info.add_row("Timezone", f"{timezone['id']}{utc}")
        isp = connection.get("org") or connection.get("isp")
        if isp:
            info.add_row("ISP", str(isp))
        if connection.get("asn"):
            info.add_row("ASN", str(connection["asn"]))
        if connection.get("domain"):
            info.add_row("ISP domain", str(connection["domain"]))
    else:
        info.add_row("Details", "[dim]Geolocation lookup unavailable[/]")

    console.print(info)
    console.print()


def show_result(ipv4: dict, ipv6: dict, geo: dict) -> None:
    """Single entry point used by main.py for a full lookup."""
    show_ip_info(ipv4, ipv6, geo)
