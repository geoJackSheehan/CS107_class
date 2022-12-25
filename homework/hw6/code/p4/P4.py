#!/usr/bin/env python3
# File       : P4.py
# Description: Priority queue implementations
# Copyright 2022 Harvard University. All Rights Reserved.
from abc import (ABC, abstractmethod)
from heapq import (heappush, heappop)

import matplotlib.pyplot as plt

from P3 import MinHeap

try:
    from merge_lists_benchmark import benchmark
except ImportError:
    pass


class PriorityQueue(ABC):
    """Priority queue base class."""

    def __init__(self, max_size):
        """
        Initialize a priority queue.

        Parameters
        ----------
        max_size : int
            Maximum element capacity of priority queue.

        """
        self._elements = []
        self._max_size = max_size

    def __len__(self):
        return len(self._elements)

    @abstractmethod
    def put(self, value):
        """
        Put (insert) an element into the priority queue.

        Parameters
        ----------
        value :
            New element value to be inserted.

        Raises
        ------
        IndexError
            If the maximum capacity is reached.

        """
        raise NotImplementedError

    @abstractmethod
    def get(self):
        """
        Get and remove the highest priority element from the priority queue.

        Returns
        -------
        value
            The element with the highest priority.

        Raises
        ------
        IndexError
            If the queue is empty.

        """
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        """
        Get the highest priority element from the priority queue without
        removing it.

        Returns
        -------
        value
            The element with the highest priority.

        Raises
        ------
        IndexError
            If the queue is empty.

        """
        raise NotImplementedError


class NaivePriorityQueue(PriorityQueue):
    # TODO part a.)
    pass


class HeapPriorityQueue(PriorityQueue):
    # TODO part b.)
    pass


class BuiltinHeapPriorityQueue(PriorityQueue):
    # TODO part b.)
    pass


if __name__ == "__main__":
    # check merged lists
    # benchmark(2, NaivePriorityQueue, list_length=3, n_samples=1, debug=True)

    # generate plot
    n_lists = list(range(1, 502, 50))
    # TODO: part c.)
