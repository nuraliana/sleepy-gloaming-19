"""Write a one-line invented-city weather forecast to entry.txt.

The forecast line is held as a single constant. The script resolves the
destination folder from MAKEFUN_OUTPUT_DIR (falling back to /output),
creates it if needed, and writes the line verbatim with no trailing
newline, so the file holds exactly the entry and nothing else.
"""

import os

ENTRY = "Gloamingford: fog till eight, then gold \u2014 the 7:55 bus is on time, and the sunrise apologises for Monday."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
