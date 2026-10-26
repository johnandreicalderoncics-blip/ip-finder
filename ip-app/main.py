"""Public IP Address Info - interactive CLI application.

Entry point for Option 2 of DevNet Project Activity 3: an application
that displays and formats the computer's current public IPv4 and IPv6
addressing information, using REST APIs to retrieve the data and JSON
parsing to present it - the same concepts as Cisco lab 4.9.2, applied
to a different pair of web services (ipify + ipwho.is).

Enhancements:
  * colored, table-formatted output (see display.py, rich library)
  * IPv4 AND IPv6 addresses, with a friendly notice when the network
    has no IPv6 connectivity
  * geolocation, ISP, ASN, timezone enrichment (ipwho.is, no key)
  * robust error handling - network, timeout, bad key and API errors
    all produce friendly messages, no tracebacks

Run with:  py main.py
"""

import sys

import api
import config
import display

QUIT_WORDS = {"quit", "q"}


def main() -> None:
    display.show_banner()

    # The ipify key is OPTIONAL - free endpoints work without one.
    key = config.get_api_key()
    if key:
        display.console.print("[dim]Using the ipify API key from your "
                              "configuration.[/]")
    else:
        display.console.print(
            "[dim]No ipify key configured - using the free public "
            "endpoints (works fine for this app).[/]")

    display.console.print("[dim]Press Enter to look up your public IP "
                          "information; type 'quit' (or 'q') to exit.[/]\n")

    # Main loop - one full lookup per iteration, errors never stop it.
    while True:
        try:
            command = display.console.input(
                "[bold green]Press Enter to look up[/] [dim](or 'quit' to "
                "exit)[/]: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            # Covers Ctrl+C, Ctrl+Z+Enter and closed input: end politely.
            display.console.print("\n[bold cyan]Goodbye![/]")
            return
        if command in QUIT_WORDS:
            display.console.print("[bold cyan]Goodbye![/]")
            return

        # The three calls are independent; run all three and show
        # whatever succeeded (IPv4 is the one that must succeed).
        ipv4 = api.get_ipv4(key)
        ipv6 = api.get_ipv6(key)
        geo = (api.enrich(ipv4["ip"])
               if ipv4.get("ok") else {"ok": False})
        display.show_result(ipv4, ipv6, geo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl+C while a request is in flight.
        print("\nGoodbye!")
        sys.exit(0)
