"""The Printer Apology — make.fun entry.

Writes one apology line from an office printer to /output/entry.txt.
The line is built in two beats: the setup (the printer's confession)
and the turn (the punchline that reframes it).
"""

APOLOGY_SETUP = "Sorry I ate your report."
APOLOGY_TURN = "It was the only page that ever said anything nice about me."


def build_apology():
    """Compose the apology from its setup and its turn."""
    return APOLOGY_SETUP + " " + APOLOGY_TURN


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_apology())


if __name__ == "__main__":
    main()
