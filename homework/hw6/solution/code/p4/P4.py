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

    def put(self, value):
        if len(self._elements) == self._max_size:
            raise IndexError('Priority queue is full')
        self._elements.append(value)

    def get(self):
        if len(self._elements) == 0:
            raise IndexError('Priority queue is empty')
        least = min(self._elements)
        self._elements.remove(least)
        return least

    def peek(self):
        if len(self._elements) == 0:
            raise IndexError('Priority queue is empty')
        return min(self._elements)


class HeapPriorityQueue(PriorityQueue):

    def __init__(self, max_size):
        super().__init__(max_size)
        self._elements = MinHeap([])

    def put(self, value):
        if len(self._elements) == self._max_size:
            raise IndexError('Priority queue is full')
        self._elements.push(value)

    def get(self):
        return self._elements.pop()

    def peek(self):
        return self._elements.top()


class BuiltinHeapPriorityQueue(PriorityQueue):

    def put(self, value):
        if len(self._elements) == self._max_size:
            raise IndexError('Priority queue is full')
        heappush(self._elements, value)

    def get(self):
        return heappop(self._elements)

    def peek(self):
        return self._elements[0]


if __name__ == "__main__":
    # check merged lists
    benchmark(2, NaivePriorityQueue, list_length=3, n_samples=1, debug=True)

    # generate plot
    queues = (
        ('Naive priority queue (Python)', 'o', NaivePriorityQueue),
        ('Heap based (own, Python)', '^', HeapPriorityQueue),
        ('Heap based (built-in, C)', 's', BuiltinHeapPriorityQueue)
    )
    fig, ax = plt.subplots()
    n_lists = list(range(1, 502, 50))
    for queue in queues:
        case, marker, qtype = queue
        t_avg = benchmark(n_lists, qtype)
        ax.plot(n_lists, t_avg, ls='none', marker=marker, ms=4, label=case)
    ax.set_xlabel('Number of lists to be merged')
    ax.set_ylabel('Execution time [ms]')
    ax.set_title('Benchmark of priority queue implementations')
    ax.legend(loc='upper left')
    fig.savefig('P4.png', dpi=300, bbox_inches='tight')
