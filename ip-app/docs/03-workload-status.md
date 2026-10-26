# Deliverable 3 - Project Workload and Status (Option 2)

**Project Activity 3 - DEVASC**
**Team:** John Andrei Calderon, Sofia Beatriz Estioco, Ken Gultiano, Lawrence Ng (Scrum Leader)
**Sprint window:** October 25-27, 2026 (presentation October 28)

## Our strategy

The same approach as our Option 1 sprint, applied to a smaller codebase:
a **single short sprint with always-runnable increments** - after every
task the application still runs, and each completed feature is committed
to its own branch and merged by pull request. The work is divided by
module (API layer, display layer, configuration, error handling) so
members can work in parallel without touching the same files. Task
status is tracked in the table below (mirrored in a shared Google Sheet
the Scrum Leader maintains) and every member posts a short update in the
group chat when they finish or get blocked. The deadline risk is managed
by priority order: the features marked **High** are the committed scope,
and stretch items are cut first if we fall behind.

## Task list, priority and status

| # | Task | Owner | Priority | Status |
|---|---|---|---|---|
| 1 | Project selection + rationale (Deliverable 1) | All (facilitated by Lawrence) | High | Done |
| 2 | Team roles and skillsets (Deliverable 2) | Lawrence | High | Done |
| 3 | Repository setup: repo, collaborators, `.gitignore`, `requirements.txt` | John Andrei | High | In progress |
| 4 | API research and selection (ipify + ipwho.is vs ipapi.co/ipstack) | All | High | Done |
| 5 | Baseline app: IPv4/IPv6 lookup loop | John Andrei | High | Done |
| 6 | API layer: enrichment + robust error handling | Ken | High | Done |
| 7 | Display layer: colored tables/panels with `rich` | Sofia | High | Done |
| 8 | Optional ipify key support (env var + config file) | John Andrei | Medium | Done |
| 9 | README: setup, usage, error reference, continuation guide | Lawrence + Sofia | High | Done |
| 10 | Verification matrix: real networks, no-IPv6, no network, quit | Ken + All | High | Done |
| 11 | Final presentation (slides + demo script) | Lawrence + All | High | To do (due Oct 28) |
| 12 | Backlog list for Project Activity 4 | Ken | Medium | Done |

## Workload expectations

Each member has other classes and commitments this week, so we agreed
on roughly **3-4 focused hours each inside the sprint window**, with
the Scrum Leader re-checking progress twice a day and reassigning
tasks if anyone is blocked. Option 2's smaller scope means the
application tasks (5-8) finished ahead of the documentation tasks,
leaving buffer time for the presentation.

## Definition of done

A task is **Done** only when: the code runs on the owner's machine, a
teammate has reviewed the pull request, and the feature appears in the
verification matrix with a passing result.

## Verification matrix

| Scenario | Expected |
|---|---|
| Normal lookup (Wi-Fi) | IPv4 + geo/ISP/ASN table; IPv6 or a friendly notice |
| No key configured | Free endpoints used, app works the same |
| Garbage key | Free endpoints still answer; app works |
| No network | Red "No network connection" panel, loop continues |
| Service timeout | Red timeout panel, loop continues |
| `q` / `quit` / Ctrl+C / EOF | Clean "Goodbye!" exit 0 |

## Backlog for Project Activity 4 (future enhancements)

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
