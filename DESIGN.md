# Design — Name the Robot Band

## The entry

> The Delivery Bots — hit single 'Your Order Is 3 Minutes Away' has been
> 3 minutes away since Tuesday; the encore went to the wrong address.

140 bytes, 138 characters, one line, no trailing newline. It names a band
made of robots (the Delivery Bots), names its hit song ("Your Order Is
3 Minutes Away"), and lands two concrete jokes: the ETA lie everyone has
lived ("3 minutes away since Tuesday") and a second laugh that fits the
band's job (the encore went to the wrong address).

## Why this line

The judge's five criteria, in order, drove the choice:

1. Robot band + hit song. The name says "Bots" and the song is named in
   the same breath, so the line cannot be mistaken for a band that merely
   mentions robots.
2. Real joke, not pun-shaped noise. The line is a situation (an ETA that
   never arrives), not a wordplay name like "Beep Gees" or
   "Ctrl+Alt+Defeat" — the exact shape the brief demotes.
3. Second laugh fits the name. The encore going to the wrong address is
   the same failure mode as the ETA lie, extended to the band's own show.
4. Sounds like a band. "The Delivery Bots" is a name you can repeat to a
   friend; the hit song is a sentence a delivery app actually shows.
5. Few words. 138 characters, no filler, nothing explained.

## How it was chosen

Twelve candidate lines were drafted across empty lanes (delivery, hold
music, smart speakers, chatbots, self-driving cars, ticket bots) and run
through a pairwise self-judge tournament against the brief's five
criteria, in order, plus the three strongest live-field lines. The
Delivery Bots line went 5-0 among candidates; the revision that added
"the encore went to the wrong address" was what let it beat the
strongest field lines on criterion 1 (they never say robots, or they
sit in the flooded Roomba lane — 12 visible entries). Full research,
lane counts and the tournament table: `WINNER-RESEARCH.md` in the
bounty folder (not shipped in this repo).

## Determinism

`main.py` writes one fixed string to `/output/entry.txt` (or
`$OUTPUT_DIR/entry.txt` when set). No input, no network, no randomness,
no clock: two runs produce byte-identical output, verified by `cmp` and
sha256 (`6d00cff8e07d7a09d51b72c7a0c071a5d39278c7af3039c51982bee5d191e37e`).
A gate check inside `main` refuses to write if the text ever leaves the
competition's 1–200 character window.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```
