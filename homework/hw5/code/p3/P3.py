#!/usr/bin/env python3
# File       : P3.py
# Description: Binary search tree
# Copyright 2022 Harvard University. All Rights Reserved.


class Node:
    """
    Node type for a binary tree.

    A node is identified by a key `key` and holds a value `val`.  The `key` is
    used for comparison using comparison operators.  A node `A` is smaller than
    a node `B` if A.key < B.key.  The value `val` can be of any type and
    represents the data stored in the tree.  Each value is identified by a
    `key`.

    """

    def __init__(self, key, val, *, left=None, right=None):
        """
        Construct a node in a binary tree.

        Parameters
        ----------
        key :
            Node key.  Must support comparison operators
        val :
            Node value.
        left : Node, None
            Left child.
        right : Node, None
            Right child.
        """
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = 1


class BinarySearchTree:

    @staticmethod
    def _subtree_size(node):
        """Return the size of the subtree with root at `node`."""
        return node.size if node is not None else 0

    def __init__(self):
        """Construct an empty tree."""
        self._root = None

    def __str__(self):
        """Formatted string representation of binary tree."""
        return self._print_tree(self._root).strip()

    def __len__(self):
        """Return the number of nodes in the tree."""
        return self._subtree_size(self._root)

    def _print_tree(self, node, indent=0):
        """Recursively print the subtree with root at `node`."""
        if node is None:
            return 'None\n'
        value = ''
        value += f'Node(key={node.key}, val={node.val})\n'
        offset = 9 * ' ' * indent
        value += offset + 'left  -> ' + self._print_tree(node.left, indent + 1)
        value += offset + 'right -> ' + self._print_tree(node.right, indent + 1)
        return value

    def _put(self, node, key, val):
        # TODO: task a.)
        pass

    def _get(self, node, key):
        # TODO: task b.)
        pass

    # Public interface
    def put(self, key, val):
        """
        Insert (put) a new node into the tree.

        Parameters
        ----------
        key :
            Node key.  Must support comparison operators
        val :
            Node value.

        Returns
        -------
        None
            The method does not return anything.

        """
        self._root = self._put(self._root, key, val)

    def get(self, key):
        """
        Get the value `val` of a tree node identified by `key`.

        Parameters
        ----------
        key :
            Node key.  Must support comparison operators

        Returns
        -------
        val :
            The value `val` of a tree node identified by `key`.

        """
        return self._get(self._root, key)


if __name__ == "__main__":
    # TODO: add your test code here
    pass
