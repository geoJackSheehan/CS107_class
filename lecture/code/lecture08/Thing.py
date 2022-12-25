#!/usr/bin/env python3
# File       : Thing.py
# Description: `Thing` class to study basic OOP design
# Copyright 2022 Harvard University. All Rights Reserved.

class Thing:
    """Simple class for a 'thing'"""
    def __init__(self, thing):
        self.state = thing

    def __str__(self):
        return f"{self.state}"

    def __add__(self, other):
        """This method implements addition '+'"""
        print(self.state)
        return Thing(f"{str(self)} + {str(other)}")

    def __iadd__(self, other):
        """This method implements augmented addition assignment '+='"""
        print(self.state)
        self.state = f"{str(self)} + {str(other)}"
        return self


def mutate(x):
    y = Thing('B')
    x += y  # calls __iadd__: study line 23
    return x


def rebind(x):
    y = Thing('C')
    x = x + y  # calls __add__: study line 17
    return x


if __name__ == "__main__":
    A = Thing('A')
    B = mutate(A)  # after this function call A and B are the same object
    C = rebind(A)  # after this function call A and C are two different objects
    print(f"id(A) = {id(A)}")
    print(f"id(B) = {id(B)}")
    print(f"id(C) = {id(C)}")
