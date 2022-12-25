#!/usr/bin/env python3
# File       : P2.py
# Description: @property decorator
# Copyright 2022 Harvard University. All Rights Reserved.

class Animal:

    # class attribute for species that exist in universe
    _species_universe = [
        'cat', 'dog', 'duck', 'elf', 'goblin', 'horse', 'human', 'mermaid',
        'nightingale', 'pig', 'swan', 'wolf'
    ]

    @staticmethod
    def _valid_species(s):
        if s not in Animal._species_universe:
            raise ValueError(f'Species `{s}` does not exist in universe')

    def __init__(self, name, species):
        self._valid_species(species)
        self.name = name
        self._species = species

    def __repr__(self):
        cls = type(self)
        return f"{cls.__name__}('{self.name}', '{self.species}')"

    # TODO: implement getter, setter and deleter for `self._species` data
    # attribute using @property decorator
