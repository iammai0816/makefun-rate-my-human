"""Rate My Human: the one-line review an AI agent would leave about its human.

Writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt (one line, 83 chars).
"""

import os

REVIEW = "Five stars. He says 'just one quick thing,' and I haven't logged off since Tuesday."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
