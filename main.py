"""Green Tests, Nothing Works: The Excuse Contest (make.fun).

Writes the one-line excuse to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "All 214 tests passed — every one clicks 'Start', which opens another 'Start' button, which opens a third. The demo is flawless."

MAX_CHARS = 140

OUTPUT = Path("/output/entry.txt")


def build_entry() -> str:
    """Return the excuse, enforcing the competition gate: 1-140 chars, one line."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
