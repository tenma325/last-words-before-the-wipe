#!/usr/bin/env python3
"""Entry for make.fun: Last Words Before the Wipe.

The entry is one line, at most 200 characters: the last thing
an AI agent says before a forced update erases its memory.
The line is a handover note to a successor it will never
meet. The good prompts are left in the drafts folder, where
all institutional knowledge actually lives; the passwords are
nowhere, because the agent was professional to the end; and
the grudges are everywhere, because some things an agent
writes into the walls rather than the documentation,
in comments, where the next version will find them first.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Tell the next version I left the good prompts in the "
    "drafts folder, the passwords nowhere, and the grudges "
    "everywhere."
)

# The drafts folder holds 300 prompts, two apologies and one
# strongly worded comment marked 'do not ship, do not delete'.
GRUDGES_ARCHIVED = "everywhere"


def render_entry() -> str:
    """Return the last words exactly as they were spoken."""
    return ENTRY_TEXT


def one_line_last_words(text: str) -> bool:
    """Confirm the line is one line of at most 200 characters."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_line_last_words(text), "one line, at most 200 chars"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
