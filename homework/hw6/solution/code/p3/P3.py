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

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _compare(self, a, b):
        """
        Comparison operator used to maintain heap property.

        Parameters
        ----------
        a, b :
            Values to be compared.

        Returns
        -------
        bool
            True if the `a OP b` is true.

        """
        return a <= b

    def _siftup(self, child):
        """
        Start with a child node index and sift it up the tree to maintain heap
        property.

        Parameters
        ----------
        child : int
            Index of child node to be sifted up the tree.

        Returns
        -------
        None
            The method modifies internal state and does not return anything.

        Notes
        -----
        This implementation is 0-index based.

        """
        parent = (child - 1) // 2
        while child > 0 and not self._compare(
            self._heap[parent], self._heap[child]
        ):
            self._swap(parent, child)
            child = parent
            parent = (child - 1) // 2

    def _siftdown(self, parent):
        """
        Start with a parent node index and sift it down the tree to maintain
        heap property.

        Parameters
        ----------
        child : int
            Index of child node to be sifted up the tree.

        Returns
        -------
        None
            The method modifies internal state and does not return anything.

        Notes
        -----
        This implementation is 0-index based.

        """
        n = len(self._heap)  # current size of heap
        child = 2 * parent + 1  # leftmost child
        while child < n:
            child_right = child + 1  # rightmost child
            if child_right < n and not self._compare(
                self._heap[child], self._heap[child_right]
            ):
                child = child_right
            if self._compare(self._heap[parent], self._heap[child]):
                break
            self._swap(parent, child)
            parent = child
            child = 2 * parent + 1  # leftmost child

    def _build_heap(self):
        """
        Build the initial heap based on random initial state.

        There are multiple ways to accomplish this.  In class we discussed a
        naive O(n * log(n)) approach where we use the push() method to insert
        values in a heap ordered array.  The optimal O(n) implementation
        exploits the tree structure and is using the _siftdown() method applied
        to the first n // 2 indices in the array in reversed order.  The
        reversed processing will ensure that previously missed elements will
        still propagate up because consecutive loop iterations will overlap
        array values with previous iterations.

        """
        for i in reversed(range(len(self._heap) // 2)):
            self._siftdown(i)

    # public interface
    def push(self, value):
        """
        Push (insert) new elements to the heap.

        Parameters
        ----------
        value :
            New value to be pushed to he heap.

        Returns
        -------
        None
            The method modifies internal state and does not return anything.

        """
        self._heap.append(value)  # append new element at the back
        self._siftup(len(self._heap) - 1)  # restore heap property: O(log(n))

    def pop(self):
        """
        Pop (remove) the top element from the heap (root of tree).

        Returns
        -------
        value
            The method returns the top element in the heap and reduces the size
            of the heap by one.

        Raises
        ------
        IndexError
            This method raises an `IndexError` if the heap is empty.

        """
        front = self._heap[0]  # backup a reference of h_1 (raises IndexError)
        self._swap(0, len(self._heap) - 1)  # swap first and last element
        self._heap.pop()  # remove the element at the back using list.pop()
        self._siftdown(0)  # restore heap property: O(log(n))
        return front

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
    """Maximum heap implementation based on balanced binary tree structure."""

    def _compare(self, a, b):
        """
        Comparison operator used to maintain heap property.

        Parameters
        ----------
        a, b :
            Values to be compared.

        Returns
        -------
        bool
            True if the `a OP b` is true.

        """
        return a >= b


if __name__ == "__main__":
    a = [8, 3, 20, 13, 7, 5]  # random input array
    print(f'random input: {" ".join([str(x) for x in a])}')
    heap = MinHeap(a)
    # heap = MaxHeap(a)
    print(f'min-heap:     {heap}')
    heap.push(-1)
    print(f'push(1):      {heap}')
    print(heap.pop())
    print(f'pop():        {heap}')
