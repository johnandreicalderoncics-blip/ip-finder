# Public IP Address Info - CLI (Option 2)

A Python command-line application that displays and formats the
computer's current **public IPv4 and IPv6** addressing information -
plus geolocation, ISP and ASN details - using REST APIs.

Built by our team for **Option 2** of Cisco DevNet Project Activity 3
(a new application that provides IP addressing information to network
technicians), applying the same REST + JSON concepts as lab 4.9.2,
*Integrate a REST API in a Python Application*.

## Team

| Member | Role |
|---|---|
| John Andrei Calderon | Developer - baseline code, configuration, GitHub repo |
| Sofia Beatriz Estioco | Developer - table/color output (display layer) |
| Ken Gultiano | Developer - error handling, quality assurance |
| Lawrence Ng | Scrum Leader - project tracking, documentation |

## REST APIs used (both free)

| API | Purpose | Key needed? |
|---|---|---|
| [ipify](https://www.ipify.org/) | Public IPv4 (`api.ipify.org`) and IPv6 (`api6.ipify.org`) addresses | Optional - free endpoints work without one; a key only raises limits |
| [ipwho.is](https://ipwho.is/) | Geolocation, ISP, ASN, timezone for the IPv4 address | No key at all |

> We chose these after comparing options (ipapi.co, ipstack): ipify and
> ipwho.is need **no credit card and no billing information**, answer in
> simple JSON, and are reliable for classroom use.

## Features (enhancements)

1. **Colored, table-formatted output** - one summary table with the
   [rich](https://github.com/Textualize/rich) library; errors appear as
   red panels, never raw tracebacks.
2. **IPv4 AND IPv6** - shows both addresses; if the network has no IPv6
   connectivity, a friendly notice is shown instead of an error.
3. **Network technician details** - location (city/region/country),
   coordinates, timezone, ISP name, ASN and ISP domain.
4. **Optional API key** - works with zero configuration; adding an ipify
   key raises rate limits.
5. **Robust error handling** - no network, timeouts and API errors
   produce friendly messages and keep the app running.

## Requirements

- Python 3.10 or newer
- The `requests` and `rich` packages:

```
py -m pip install -r requirements.txt
```

> On Windows use the `py` launcher as shown. If `python` opens the
> Microsoft Store instead, that is the Windows Store alias - `py` avoids it.

## API key setup (optional)

The app runs without any key. To use one (free at
<https://www.ipify.org/> - sign up, then copy the key from the
dashboard), set it up in **either** of these ways:

**Option A - environment variable**

```
setx IPIFY_KEY "your-key-here"
```

Open a **new** terminal afterwards so the variable takes effect.

**Option B - config file**

1. Copy `config.sample.ini` in this folder and name the copy `config.ini`.
2. Replace `YOUR_KEY_HERE` with your key.

`config.ini` is listed in `.gitignore`, so your key will **not** be
committed to GitHub. Never paste a real key into any other file.

## Usage

```
py main.py
```

Press Enter to look up your public IP information; type `quit` or `q`
to exit. Sample session:

```
Press Enter to look up (or 'quit' to exit):
+-------------------------------------------------------------------------+
|         IPv4  |  203.0.113.42                                           |
|         IPv6  |  Not available on this network                          |
|     Location  |  Angeles City, Central Luzon, Philippines               |
|  Coordinates  |  15.1535, 120.5833                                      |
|     Timezone  |  Asia/Manila (UTC +08:00)                               |
|          ISP  |  Converge ICT                                           |
|          ASN  |  17639                                                  |
|   ISP domain  |  convergeict.com                                        |
+-------------------------------------------------------------------------+
```

Re-running the lookup after switching networks (e.g. Wi-Fi to mobile
hotspot) shows the new address - useful for demonstrating to network
technicians how public addressing changes per connection.

## Project structure

| File | Purpose |
|---|---|
| `main.py` | Entry point: banner, lookup loop, quit/Ctrl+C handling |
| `config.py` | Loads the optional ipify key (env var `IPIFY_KEY`, then `config.ini`) |
| `api.py` | All REST calls (ipify IPv4/IPv6, ipwho.is enrichment); converts every failure into a plain result dictionary |
| `display.py` | All output: rich tables/panels |
| `config.sample.ini` | Template for the git-ignored `config.ini` |
| `requirements.txt` | Third-party dependencies |
| `docs/` | Project deliverables 1-3 (selection, roles, workload) |

## Error handling reference

| Situation | What the user sees |
|---|---|
| No internet / DNS failure | Red panel: "No network connection" |
| API slower than 10 s | Red panel: "The request timed out" |
| Rejected API key (HTTP 401/403) | Red panel: how to fix the key |
| Network with no IPv6 | Yellow notice: "IPv6 - Not available on this network" |
| Geolocation service down | Table still shows the addresses, details row says unavailable |
| `Ctrl+C` / `quit` / end of input | "Goodbye!" and a clean exit |

## Future enhancements (backlog)

Tracked for Project Activity 4 (details in `docs/03-workload-status.md`):

1. Continuous watch mode that refreshes on an interval
2. Detect when the public IP changes and highlight it
3. Multi-API fallback chain (ipify -> ipapi.co -> ipinfo.io)
4. Export the report to JSON/text for tickets
5. IPv6 readiness score with an explanation for technicians
6. Local/private IP display alongside the public IPs
7. Command-line arguments (`argparse`) for non-interactive use
8. Unit tests with `pytest` and mocked API responses
9. Cache the last lookup to avoid duplicate API calls
10. Web front-end (Flask) reusing `api.py`

## Contributing / continuation guide

Our team workflow: each member works on a branch, opens a pull request,
and another member reviews before merging into `main`.

To add a feature, touch the module that owns that concern:

- New prompt/loop behavior -> `main.py`
- New API call or provider -> `api.py` (keep failures as
  `{"ok": False, ...}` dictionaries so display stays simple)
- New rows/columns/formatting -> `display.py`
- New configuration -> `config.py`

Keep the layers separate: `api.py` never prints, `display.py` never
calls the network, and `main.py` only orchestrates.
