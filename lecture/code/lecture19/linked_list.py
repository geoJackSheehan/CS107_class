#!/usr/bin/env python3
# vim: foldmethod=marker
# File       : linked_list.py
# Description: Linked list example with generator function for __iter__
# Copyright 2022 Harvard University. All Rights Reserved.
import copy


# Node {{{1
class Node:
    def __init__(self, key, *, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


# LinkedList {{{1
class LinkedList:
    # List creation {{{2
    def __init__(self, key, data, *, reverse=False):
        start = Node(key[0], data=data[0])  # create root node
        end = start
        for k, d in zip(key[1:], data[1:]):
            if reverse:
                end = self._prepend(end, Node(k, data=d))
            else:
                end = self._append(end, Node(k, data=d))
        self.first = end if reverse else start

    @staticmethod
    def _append(anchor, node):
        anchor.next = node
        return node

    @staticmethod
    def _prepend(anchor, node):
        node.next = anchor
        return node

    # Sequence properties {{{2
    def __getitem__(self, key):
        _, node = self._getitem(key)
        return node

    def __len__(self):
        node = self.first
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        node = self.first
        pretty = ""
        while node != None:
            pretty += f"node: {hex(id(node))} : key={node.key} : data={node.data}\n"
            node = node.next
        return pretty

    def _getitem(self, key):
        """Private method to retrieve a list element given a key.
           Arguments:
              key: identifies the node
           Returns:
              Tuple with reference to predecessor node and reference to node
              with given key
        """
        node = self.first
        prev = node
        while node != None:
            if node.key == key:
                return (prev, node)
            prev = node
            node = node.next
        raise KeyError(f"Key '{key}' not found")

    # Node insertion {{{2
    def insert(self, key, node, *, before=False):
        anchor = self.__getitem__(key)
        if before:  # insert before
            tmp = copy.copy(anchor)  # beware!
            anchor.key = node.key
            anchor.data = node.data
            node = tmp
            anchor.next = node
        else:  # insert after
            assert anchor is not None
            node.next = anchor.next
            anchor.next = node
        return node

    # Node removal {{{2
    def remove(self, key):
        if self.first.key == key:
            del_node = self.first
            self.first = self.first.next
        else:
            prev, del_node = self._getitem(key)
            prev.next = del_node.next
        del del_node

    # Iterator {{{2
    def __iter__(self):
        node = self.first
        while node != None:
            yield node
            node = node.next


# main() {{{1
def main():
    # create a list
    linked_list = LinkedList(range(5), list('abcde'))

    # iter(ll) returns a generator object
    print(type(iter(linked_list)))
    for node in linked_list:
        print(f'{node} : key={node.key} value={node.data}')


if __name__ == "__main__":
    main()
