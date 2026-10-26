# Deliverable 2 - Team Roles (Option 2)

**Project Activity 3 - DEVASC**
**Team:** John Andrei Calderon, Sofia Beatriz Estioco, Ken Gultiano, Lawrence Ng (Scrum Leader)

## Roles and responsibilities

| Member | Primary role | Responsibilities in this project |
|---|---|---|
| **Lawrence Ng** | Scrum Leader | Facilitates planning, maintains the task list and status board, runs the daily check-in, owns the GitHub workflow (branches, pull requests, merges), assembles the final presentation |
| **John Andrei Calderon** | Developer / Repo owner | Creates and administers the GitHub repository, invites collaborators, builds the application baseline and configuration module, sets up `.gitignore` and dependency files |
| **Sofia Beatriz Estioco** | Developer | Implements the colored, table-formatted output layer (rich tables/panels), ensures the information reads clearly for network technicians, contributes to documentation |
| **Ken Gultiano** | Developer / QA | Implements the error-handling layer (network, timeout, key, service errors, no-IPv6 case), designs and runs the verification matrix, logs defects and verifies fixes |

## Knowledge and skillsets each member brings

- **Lawrence Ng** - organization and coordination; keeps meetings short
  and decisions recorded; experience tracking work in shared sheets.
- **John Andrei Calderon** - Python and REST API fundamentals from lab
  4.9.2; Git/GitHub experience; comfortable wiring configuration and
  environment setup.
- **Sofia Beatriz Estioco** - eye for presentation and formatting;
  quick with Python libraries and making console output readable.
- **Ken Gultiano** - systematic testing mindset; patience for edge
  cases (no IPv6 connectivity, timeouts, service outages) that other
  teams forget.

## Cross-training plan

Working in one shared repository means every pull request is reviewed
by a second member, so each feature's author explains their code to the
reviewer - a built-in cross-training loop. For this option the
pairings are: John Andrei walks the team through the API layer
(`api.py`, including how the two REST providers differ), Sofia through
the display layer (`display.py`), and Ken through the failure paths he
tested. Because the option-1 codebase uses the same three-layer design,
each member can switch between options after one walkthrough.
