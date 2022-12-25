#!/usr/bin/env python3
# File       : FrenchDeck.py
# Created    : Fri Sep 17 2021 08:12:06 PM (-0400)
# Description: Code based on Example 1-1 Fluent Python: Clear, Concise, and
#              Effective Programming by Luciano Ramalho (O'Reilly Media, 2015)
# Copyright 2021 Harvard University. All Rights Reserved.
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """French deck of 52 playing cards"""
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """Initialize ordered deck of cards"""
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        """Return length of deck"""
        return len(self._cards)

    def __getitem__(self, index):
        """Return card at index"""
        return self._cards[index]

    def __setitem__(self, index, card):
        """Set a card at index"""
        self._cards[index] = card  # this method does not return a value

    def __str__(self):
        """Pretty print card deck"""
        map_utf8 = {
            'clubs': '♣',
            'diamonds': '♦',
            'hearts': '♥',
            'spades': '♠'
        }
        cpl = 13  # number of cards per printed line
        pretty = []
        for line in range((len(self._cards) + cpl - 1) // cpl):
            for card in self._cards[line * cpl:(line + 1) * cpl]:
                pretty.append(f"  {card.rank:>2}{map_utf8[card.suit]}")
            pretty.append('\n')
        return ''.join(pretty).rstrip()
