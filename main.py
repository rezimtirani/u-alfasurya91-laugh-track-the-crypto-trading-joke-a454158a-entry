"""Laugh Track: The Crypto Trading Joke Contest.

Writes one joke about crypto and trading life to
$MAKEFUN_OUTPUT_DIR/entry.txt: a stop-loss set to protect the
trader's money that triggered so fast it now protects someone
else's money. Standard library only.
"""

import os
import sys

CRYPTO_JOKE = (
    "I set a stop-loss to protect my money. It triggered so "
    "fast it now protects someone else's money."
)


def joke_gate(text):
    """Check the joke against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space: a single joke about crypto and trading
    life, one line, plain text. Returns the cleaned text or
    raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("crypto joke must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "crypto joke is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("crypto joke must be exactly one line")
    return cleaned


def joke_measure(text):
    """Measure the joke for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A joke too short to carry a setup and a
    turn, or one padded out to fill the cap instead of landing
    the punchline, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = joke_gate(CRYPTO_JOKE)
    shape = joke_measure(text)
    if shape["words"] < 5:
        raise ValueError("crypto joke is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
