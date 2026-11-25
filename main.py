#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

A phone battery, down to its last percent, finally texts the charger
it has been waiting for all day. The joke is the battery treating the
5% warning like a terms-of-service popup: swiped away unread, then
blamed for everything that follows.

The entry is one plain line of text, written to entry.txt inside the
directory make.fun hands us through MAKEFUN_OUTPUT_DIR.
"""

import os

# The battery's last text, exactly as it goes out: one line, 149
# characters, no trailing newline — the gate counts the whole file.
LINE = "You swiped past my 5% warning like a terms-of-service popup. Fine. I'm at 1% now, and I'm taking your unsent text with me — tell your boss I said hi."

# The competition caps the entry at 200 characters.
MAX_CHARS = 200


def resolve_output_dir():
    """Return the directory the entry file goes in.

    make.fun sets MAKEFUN_OUTPUT_DIR when it grades the entry; when
    the program runs anywhere else, fall back to /output so a smoke
    test still has somewhere to write.
    """
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    return out


def check_line(line):
    """Refuse anything that would break the entry gate."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} cap"
        )
    return line


def write_entry(out_dir, line):
    """Write the entry file and say where it landed."""
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def verify_entry(path, line):
    """Read the file back and confirm it holds exactly the line."""
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError(f"{path} does not match the entry line")


def main():
    line = check_line(LINE)
    path = write_entry(resolve_output_dir(), line)
    verify_entry(path, line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
