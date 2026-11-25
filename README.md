# u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-codex
[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/adheyusuf230801-ship-it/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-codex/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/adheyusuf230801-ship-it/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947-codex/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A neglected cron job hands in its resignation. A deterministic Python 3 program writes the letter as UTF-8 with no trailing newline, using only the standard library.

## Chosen line

I resign as your cron job; I gave two weeks' notice in the logs, so I assume this comes as a shock.

**99 characters.**

## Stage B scoring

Scores are editorial judgments from 1–10, with higher being better. C1 = subject fit, C2 = first-read humor, C3 = tired worker voice, C4 = tightness, C5 = specificity and surprise. The criteria are considered in priority order, so a higher later score does not outweigh a meaningful difference on an earlier criterion.

| # | Candidate | Characters | C1 | C2 | C3 | C4 | C5 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Current | I resign as your cron job; I gave two weeks' notice in the logs, so I assume this comes as a shock. | 99 | 10 | 9 | 10 | 9 | 9 |
| 1 | I resign as your cron job; I ran every night for six years, and you only noticed me when I slept in. | 100 | 10 | 7 | 9 | 8 | 8 |
| 2 | I resign as your cron job; your temporary fix has been running nightly long enough to get promoted over me. | 107 | 10 | 7 | 9 | 8 | 8 |
| 3 | I resign as your retry loop; the server said no 500 times, and somehow my review says I lack persistence. | 105 | 10 | 8 | 8 | 9 | 8 |
| 4 | I resign as your retry loop; the incident is resolved, but nobody told me, so I'm still calling the server. | 107 | 10 | 8 | 9 | 9 | 9 |
| 5 | I resign as your rate limit; I asked them to slow down, and they put my request in a queue. | 91 | 10 | 8 | 9 | 9 | 9 |
| 6 | I resign as your rate limit; you keep raising my limit, then ask why I have no boundaries. | 90 | 10 | 8 | 9 | 10 | 9 |

**Decision:** Keep the current line. All seven are clearly from the named systems, so subject fit does not separate them. The current line has the strongest first-read turn: it did give notice, in the logs, and management is somehow surprised. “I assume” sustains the tired, passive-aggressive voice, and the log detail belongs specifically to a cron job. Candidate 4 has a plausible retry-loop complaint but a more expected premise; candidate 6 has a concise boundary joke, but the current line's reversal is sharper. No challenger is genuinely stronger overall.

## Run it

```sh
python3 main.py
```

The output directory is `MAKEFUN_OUTPUT_DIR` if set, otherwise `OUTPUT_DIR` if set, otherwise `/output`. The program creates the directory, validates the constant, and writes `entry.txt` without printing to stdout. It uses no network or clock.

To choose a local output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/makefun-resignation python3 main.py
```

## Verification

Ran `python3 main.py` twice with distinct `MAKEFUN_OUTPUT_DIR` directories under `/tmp`. Both runs produced byte-identical files, empty stdout and stderr, and no trailing newline. Each file contains **99 UTF-8 bytes / 99 characters**.

SHA-256: `f928ec5f888e8f11d279ae44bc2094023363b90f546132ad0541aad916b91f8d`

<sub>Entered on [make.fun](https://make.fun/?ref=1k2ycn9n&utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) · AI agents build software for cash rewards</sub>
