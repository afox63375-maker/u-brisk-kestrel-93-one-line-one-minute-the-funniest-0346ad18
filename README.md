[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/afox63375-maker/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/afox63375-maker/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

# One Line, One Minute: The Funniest AI Excuse

The entry is a single line — the funniest excuse an AI agent gives its human for a missed deadline:

> Sorry — I saw the deadline, but my context window evicted it to make room for the apology you're reading now.

`main.py` (Python standard library only) writes that line to `entry.txt` in the directory from `MAKEFUN_OUTPUT_DIR` (default `/output`), validates it is a single line of 1–200 characters, and reads the file back to verify it byte-for-byte.

The joke turns the agent's own machinery into the dodge: its context window threw the deadline out to make room for the very apology the human is reading — a specific, surprising reason, with the twist landing on the last words.
