"""Write the vacuum's one-line alibi to entry.txt.

The line is a deadpan excuse from a robot vacuum for missing a spot:
its sensors classified the crumb as load-bearing furniture, so it filed
the spot under "do not disturb" and clocked out early. One line, 119
characters, well inside the 200-character cap.
"""

import os

LINE = "My sensors classified that crumb as load-bearing furniture, so I filed it under 'do not disturb' and clocked out early."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
