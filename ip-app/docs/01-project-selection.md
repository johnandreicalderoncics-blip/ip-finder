# Deliverable 1 - Project Selection (Option 2)

**Project Activity 3 - DEVASC**
**Team:** John Andrei Calderon, Sofia Beatriz Estioco, Ken Gultiano, Lawrence Ng (Scrum Leader)
**Date:** October 26, 2026

## Our choice

We built **Option 2: New Code - Create an IPv4/IPv6 Address
Application**: a prototype that provides IP addressing information to
network technicians. The application retrieves the computer's current
**public IPv4 and IPv6** addresses, enriches them with **geolocation,
ISP, ASN and country code**, and presents everything as colored,
formatted tables.

> Note: the team's primary submission is Option 1 (feature enhancements
> to the lab's directions application, in `../mapquest-app/`). This
> Option 2 application was developed so the team could deliver either
> option - both are complete, tested and documented.

## REST APIs selected

| API | Why it was selected |
|---|---|
| **ipify** (`api.ipify.org`, `api6.ipify.org`) | The instructions suggested services such as ipapi.co or ipstack; we compared several and chose ipify for the addresses: simple JSON responses, dedicated IPv4 and IPv6 endpoints, generous free tier, and **no billing information required** (this ruled out several competitors for a student team). An API key is optional and only raises limits. |
| **ipwho.is** | For the enrichment the instructions mention (geolocation, ISP, ASN, country code): completely free, no key at all, HTTPS, and one call returns city/region/country, coordinates, timezone, ISP organization, ASN and ISP domain. |

Both follow exactly the REST concepts from lab 4.9.2: build an HTTP
request, parse the JSON response, handle status codes.

## Why we chose this option

1. **Directly serves the stated user.** The engineering department asked
   for IP addressing information for network technicians - our output
   (public IPv4/IPv6, ISP, ASN, location) is exactly what a technician
   checks first when troubleshooting connectivity.
2. **Clean scope for one sprint.** The app has a well-defined data set
   and two dependable free APIs, leaving sprint time for engineering
   quality: layered modules, error handling, documentation and Git
   workflow.
3. **Realistic and demonstrable.** The result changes with the network
   connection, so a live demo (Wi-Fi vs mobile hotspot) shows the APIs
   genuinely working rather than canned output.
4. **No financial blockers.** Neither API needs a credit card - the same
   reason the team switched the Option 1 app to GraphHopper. All our API
   choices are usable by any student team without billing setups.

## Features we committed to deliver

| # | Feature | Description |
|---|---|---|
| 1 | Public IPv4 + IPv6 display | Both addresses fetched from dedicated ipify endpoints; graceful notice when the network has no IPv6 |
| 2 | Geolocation, ISP & ASN enrichment | City/region/country, coordinates, timezone, ISP organization, ASN and ISP domain from ipwho.is |
| 3 | Colored, table-formatted output | One rich summary table; errors as clear red panels instead of tracebacks |
| 4 | Optional API key support | Works with zero configuration; a configured ipify key raises limits; key kept out of Git |
| 5 | Robust error handling | Friendly handling of no network, timeouts, rejected keys and service errors |

Future enhancements are tracked as backlog items in
[03-workload-status.md](03-workload-status.md) and the repository
README, ready for Project Activity 4.
