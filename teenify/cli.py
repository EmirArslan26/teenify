from __future__ import annotations

"""Command line interface for the teenify tool.

This module defines a simple console entry point that takes a single
string argument and prints its teenified version. It deliberately
avoids external dependencies such as ``click`` to keep the tool
usable in restricted environments where installing packages might
not be possible.
"""

import argparse

from . import teenify as teenify_func


def main() -> None:
    """Parse command line arguments and print the teenified result.

    This entrypoint accepts a single positional argument (the text to
    teenify) and prints the transformed string to standard output.
    """
    parser = argparse.ArgumentParser(description="Convert text into playful teen slang.")
    parser.add_argument("text", help="The input text to be teenified.")
    args = parser.parse_args()
    print(teenify_func(args.text))


if __name__ == "__main__":
    main()
