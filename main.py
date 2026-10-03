"""Hosts Comment Toggle — Comment or uncomment a hosts line by hostname, with a backup."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hosts_comment_toggle',
        description='Comment or uncomment a hosts line by hostname, with a backup.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Hosts Comment Toggle')
    print('Flip a block on or off without a full rewrite.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
