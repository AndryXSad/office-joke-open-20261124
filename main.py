"""Office Joke Open entry.

Writes one single-line office joke to entry.txt.

The joke is a literal string held in this file: asking IT for a second
monitor earns a mindfulness lecture instead, and the punchline turns the
word "screen" into "inner peace" in the last few words.
"""

import os
from pathlib import Path

JOKE = (
    "I asked IT for a second monitor and got a lecture on mindfulness "
    "instead \u2014 apparently the screen I need is inner peace."
)


def check(joke: str) -> None:
    """Gate the joke the same way the sealed scorer does: UTF-8 text of
    1 to 200 characters, not only white space, on a single line."""
    assert joke, "joke must not be empty"
    assert joke.strip(), "joke must not be only white space"
    assert "\n" not in joke and "\r" not in joke, "joke must be one line"
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"


def main() -> None:
    check(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
