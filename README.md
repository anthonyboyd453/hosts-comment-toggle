![Hosts Comment Toggle](assets/hero.png)

# Hosts Comment Toggle

*Flip a block on or off without a full rewrite.*

## What Hosts Comment Toggle is

**Hosts Comment Toggle** is a network utility. Comment or uncomment a hosts line by hostname, with a backup.

You toggle a dev hostname all week.

It runs on the local PC. No account, and nothing is uploaded.

## What's included

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Highlights

- By hostname
- Backup
- Preview
- Does not add new hosts unless asked

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/anthonyboyd453/hosts-comment-toggle

MIT license. See `LICENSE`.
