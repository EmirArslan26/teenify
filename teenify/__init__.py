"""Teenify core module.

This module exposes a simple function ``teenify`` which takes
a string input and returns a modified version intended to mimic the
colloquial, exaggerated style associated with Turkish teen slang.
The transformation here is intentionally light‑hearted and purely for fun.

Example:

>>> from teenify import teenify
>>> teenify("Bugün derse gelmiyorum")
'Bugüünn ddeeerrssee geeelmiiyyooruum kanka 🤘😎'

"""
from __future__ import annotations


def teenify(text: str) -> str:
    """Transform plain text into playful teen speak.

    This helper exaggerates vowels and appends a slang suffix. It deliberately
    does not rely on external APIs to keep this tool usable offline and
    predictable for testing purposes.

    Parameters
    ----------
    text: str
        The input string to be teenified.

    Returns
    -------
    str
        A transformed string with repeated vowels and a signature suffix.
    """
    # Define vowel mapping: each vowel is repeated to create an exaggerated effect.
    replacements = {
        'a': 'aa', 'e': 'ee', 'ı': 'ıı', 'i': 'ii', 'o': 'oo', 'ö': 'öö',
        'u': 'uu', 'ü': 'üü', 'A': 'AA', 'E': 'EE', 'I': 'II', 'İ': 'İİ',
        'O': 'OO', 'Ö': 'ÖÖ', 'U': 'UU', 'Ü': 'ÜÜ'
    }
    # Construct the output by replacing each character if it is a vowel.
    transformed_chars = [replacements.get(ch, ch) for ch in text]
    transformed = ''.join(transformed_chars)
    # Append a friendly teen suffix. This could be further parameterised in the future.
    return f"{transformed} kanka 🤘😎"


__all__ = ["teenify"]
