#!/usr/bin/env python3
# File       : P3.py
# Description: Heap implementation (heap ordered balanced binary tree)
# Copyright 2022 Harvard University. All Rights Reserved.


class MinHeap:
    """Minimum heap implementation based on balanced binary tree structure."""

    def __init__(self, x):
        """
        Initialize and build a heap based on random array x.

        Parameters
        ----------
        x : array-like
            Input array with possibly random values.

        """
        self._heap = x
        self._build_heap()

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return ' '.join([f'{k}' for k in self._heap])

    def _compare(self, a, b):
        # TODO: part a.)
        pass

    def _siftup(self, child):
        # TODO: part a.)
        pass

    def _siftdown(self, parent):
        # TODO: part a.)
        pass

    def _build_heap(self):
        # TODO: part b.)
        pass

    # public interface
    def push(self, value):
        # TODO: part b.)
        pass

    def pop(self):
        # TODO: part b.)
        pass

    def top(self):
        """
        Get the top element from the heap (root of tree).

        Returns
        -------
        value
            The method returns the top element in the heap.

        Raises
        ------
        IndexError
            This method raises an `IndexError` if the heap is empty.

        """
        return self._heap[0]  # return h_1 (raises IndexError if heap is empty)


class MaxHeap(MinHeap):
    # TODO: part c.)
    pass


if __name__ == "__main__":
    # TODO: optional test code
    pass
