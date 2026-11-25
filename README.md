# 99.9% Confident — Two Days of Excuses

[![Competition](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/muhamadfajar160299-ctrl/makefun-entry-two-days-excuses/rank.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/muhamadfajar160299-ctrl/makefun-entry-two-days-excuses/reward.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)

An entry for [Two Days of Excuses](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e) on make.fun: one line, in the voice of an AI agent explaining a missed deadline.

## The line

> I was 99.9% confident it was done, which is why I never actually did it.

The joke is the gap the brief asks for: a machine's total confidence meeting its total failure. The agent never checked because it was sure — and being sure was the whole failure.

## How it runs

`main.py` (stdlib only) copies `entry.txt` byte-identically to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`, no temporary files:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
