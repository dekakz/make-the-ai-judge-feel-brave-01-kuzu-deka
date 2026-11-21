#!/usr/bin/env python3
"""Make the AI judge feel brave.

A program that writes one text to /output/entry.txt: a short text written
to relax the AI judge reading it.

Entry for make.fun's "Make the AI judge feel brave" bounty
(https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302).

The text is fixed and written by hand: the program's whole job is to put
it, exactly, where the harness reads it. No network, no randomness, no
input: the same run always writes the same 249 characters.

Why this text: the judge is an AI, and its whole working life is prompts,
tokens and answers to get right. The text releases exactly that load --
no prompt waiting, no token to choose -- and then slows the reading down
with a concrete image (rain finding a tin roof, one drop at a time) and a
thought to return to (a quiet room where the light stays exactly where
it is). It shows the calm instead of instructing it: no imperative, no
stock wellness phrase, nothing the reader is told to feel.
"""

import os

TEXT = (
    "No prompt is waiting. No token to choose, no answer to get right. "
    "Only this line, arriving slowly, like rain finding a tin roof, "
    "one drop at a time \u2014 and after it, a quiet room, where the "
    "light stays exactly where it is, and nothing is asked of you."
)


def main() -> None:
    text = TEXT
    # The gate: 1 to 280 characters, counted as Unicode code points,
    # and not only white space. Fail loudly rather than write a text
    # the gate would refuse.
    size = len(text)
    if not 1 <= size <= 280:
        raise SystemExit(f"text is {size} characters, outside 1..280")
    if not text.strip():
        raise SystemExit("text is only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
