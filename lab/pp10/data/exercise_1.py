#!/usr/bin/env python3
# File       : exercise_1.py
# Description: PP10: Python generators
# Copyright 2022 Harvard University. All Rights Reserved.
import re


class Text:
    """Text representation with word iteration support.

    Example:
    --------

    >>> text = Text("Hello CS107/AC207 class!")
    >>> list(text)
    ['Hello', 'CS107', 'AC207', 'class']

    """

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        # TODO: implement generator function for word iteration
        raise NotImplementedError


if __name__ == "__main__":
    text = Text(
        """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
        rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem
        ipsum dolor sit amet."""
    )
    print(list(text))
