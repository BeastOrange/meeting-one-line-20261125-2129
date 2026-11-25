"""Submission for make.fun bounty: The Meeting That Should Have Been One Line."""

from pathlib import Path

# Why this line kills the meeting:
# It names the structural truth: the group spent an hour debating choices, but
# operates with zero decision authority. Exposing that nobody in the room is
# permitted to decide anything instantly punctures the illusion and ends the meeting.
ENTRY_LINE = (
    "We spent an hour deciding nothing because nobody in this room is allowed to decide anything."
)


def validate_line(text: str) -> None:
    """Validate entry constraints: non-blank, 1-200 UTF-8 bytes, and exactly one sentence."""
    if not text or not text.strip():
        raise ValueError("Entry line must not be blank.")

    byte_len = len(text.encode("utf-8"))
    if not (1 <= byte_len <= 200):
        raise ValueError(
            f"Entry length ({byte_len} UTF-8 bytes) must be between 1 and 200 bytes."
        )

    if "\n" in text or "\r" in text:
        raise ValueError("Entry must not contain newline characters.")

    # Validate that the line constitutes exactly one sentence
    terminal_marks = [c for c in text if c in ".!?"]
    if not text.endswith((".", "!", "?")) or len(terminal_marks) != 1:
        raise ValueError(
            f"Entry must be exactly one sentence ending with a single terminal punctuation mark ('.', '!', '?'); "
            f"found {len(terminal_marks)} punctuation mark(s): {terminal_marks}."
        )


def main() -> None:
    validate_line(ENTRY_LINE)
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / "entry.txt"
    # Write the verified single-line entry
    out_file.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
