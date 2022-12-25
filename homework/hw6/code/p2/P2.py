#!/usr/bin/env python3
# File       : P2.py
# Description: Binary search tree extensions with node deletion and traversal
# Copyright 2022 Harvard University. All Rights Reserved.
from enum import Enum


class DFSOrder(Enum):
    """Depth first search order for binary tree traversal."""
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


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

    def __repr__(self):
        args = f"key={repr(self.key)}, val={repr(self.val)}"
        return f"{type(self).__name__}({args})"


class BinarySearchTree:
    """Binary search tree implementation."""

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
        """
        Insert (put) a new node into the tree.

        This method inserts a new node into the binary search tree or updates
        the value `val` if `key` exists.  It further computes the size of the
        subtree with root at `node`.

        Parameters
        ----------
        node : Node, None
            Root node of a subtree.
        key :
            Node key.  Must support comparison operators
        val :
            Node value.

        Returns
        -------
        Node
            The method returns the input node or creates a new node if `node` is
            None.

        """
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._subtree_size(node.left
                                          ) + self._subtree_size(node.right)
        return node

    def _get(self, node, key):
        """
        Get the value `val` of a tree node identified by `key`.

        Parameters
        ----------
        node : Node, None
            Root node of a subtree.
        key :
            Node key.  Must support comparison operators

        Returns
        -------
        val :
            The value `val` of a tree node identified by `key`.

        Raises
        ------
        KeyError
            If no tree node with `key` exists.

        """
        if node is None:
            raise KeyError(f'Key `{key}` not found')
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def _remove_min(self, node):
        # TODO: part a.)
        raise NotImplementedError

    def _remove(self, node, key):
        # TODO: part b.)
        raise NotImplementedError

    def _preorder(self, node):
        # TODO: part c.)
        raise NotImplementedError

    def _inorder(self, node):
        # TODO: part c.)
        raise NotImplementedError

    def _postorder(self, node):
        # TODO: part c.)
        raise NotImplementedError

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

    def remove(self, key):
        """
        Remove a node in the tree.

        Parameters
        ----------
        key :
            Key of the node to be removed.  Must support comparison operators

        Returns
        -------
        None
            The method does not return anything.

        """
        self._root = self._remove(self._root, key)

    def get_iterator(self, order: DFSOrder):
        """
        Obtain a tree iterator based on given traversal order.

        Parameters
        ----------
        order : DFSOrder
            Specifies the tree traversal order.  Can be one of
            DFSOrder.PREORDER, DFSOrder.INORDER, DFSOrder.POSTORDER.

        Returns
        -------
        Generator
            The method returns a generator object for iteration.

        """
        assert self._root is not None
        if order == DFSOrder.PREORDER:
            return self._preorder(self._root)
        elif order == DFSOrder.INORDER:
            return self._inorder(self._root)
        elif order == DFSOrder.POSTORDER:
            return self._postorder(self._root)
        else:
            raise ValueError(f"Unknown tree traversal order `{order}`")


if __name__ == "__main__":
    # TODO: optional test code
    pass
