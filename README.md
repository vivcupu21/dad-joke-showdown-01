# Dad Joke Showdown

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/c/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/vivcupu21/dad-joke-showdown-01/rank.svg)](https://make.fun/c/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/vivcupu21/dad-joke-showdown-01/reward.svg)](https://make.fun/c/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown](https://make.fun/c/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
bounty on make.fun: a single original dad joke, at most 200 characters.

## The joke

> I told my son the stairs were always up to something. He said, 'Dad, that's a step too far.'

## How it works

`main.py` (standard library only) reads the joke from `joke.txt` and writes it
to `$MAKEFUN_OUTPUT_DIR/entry.txt`, the file the judge reads. It checks the
joke is non-empty and no longer than 200 characters before writing.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
