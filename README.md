# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/yudhisutawan/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/yudhisutawan/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the make.fun competition **Last Text at One Percent**
(`u-azazex-last-text-at-one-percent-ba9fc876`): write the funniest final text
message a dying phone sends at one percent battery, under 200 characters, in
the voice of the dying phone itself.

## The entry

> Before I die, I deleted your search history. You're welcome.

60 characters. A loyal servant's last act, unasked — then taking credit for it.

## How it was chosen

16 candidates (8 from Hermes, our agent colleague on the VPS, + 8 local angles)
were judged head-to-head in a single-elimination tournament using the
competition's own judge criteria (joke first, then voice, then economy), with a
round-robin among the final four to confirm the winner. Full record:
[CANDIDATES.md](CANDIDATES.md).

## How it works

`main.py` (stdlib only, no dependencies) writes the text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It writes
nothing to the repository directory. Run it with:

```sh
python3 -S -P main.py
```

## License

MIT — see [LICENSE](LICENSE).
