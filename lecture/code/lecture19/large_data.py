#!/usr/bin/env python3
# vim: foldmethod=marker
# File       : large_data.py
# Description: Example: using generators for reading (large) data files
# Copyright 2022 Harvard University. All Rights Reserved.
import os
import argparse
from itertools import chain

import numpy as np


# argument parser {{{1
def parse_args(*, partial=False):
    parser = argparse.ArgumentParser(description="Generator example with large data.")
    # yapf: disable
    parser.add_argument('-g', '--generate', action='store_true',
            help="Generate the test data (will take up `size` MB of disk space)")
    parser.add_argument('-e', '--eager', action='store_true',
            help="Include data source obtained with eager reader.")
    parser.add_argument('-s', '--size', type=int, default=2048,
            help="Size of test data file in MB.  Default is 2048MB.")
    parser.add_argument('-c', '--chunk_size', type=int, default=1,
            help="Chunk size for lazy load of binary data file.")
    # yapf: enable
    if partial:
        return parser.parse_known_args()
    else:
        return parser.parse_args()


# process data {{{1
def process(*data_iterables):
    """
    Process data from multiple sources.

    In this example the data elements are expected to be scalars and are just
    summed up.  In practice here is where you do the actual work.

    Example:
    --------
    Note that data iterables can be iterables, iterators or generators.  The
    example below uses a list and tuple to demonstrate.

    >>> process([1, 2, 3], (4, 5))
    15

    """
    val = 0
    item_count = 0
    for item in chain.from_iterable(data_iterables):
        val += item
        item_count += 1
        if item_count % 10000 == 0:
            print(f'{item_count} items processed from input')
    return val


# data readers (generators) {{{1
# lazy binary data reader (generator) {{{2
def read_binary_lazy(fname, chunk_size=1):
    """
    Lazy binary data loader (generator).

    Load data from a binary file specific to an application.  This loader is
    using a generator to load the data lazy upon request in chunk sizes
    specified by `chunk_size`.

    Parameters
    ----------
    fname : str
        Path to data file.
    chunk_size : int
        Number of data elements to be loaded from the file.  This parameter can
        optimize the bandwidth for reading the file.  Reading small sizes from a
        file is not efficient.

    Yields
    ------
    float
        One data element from the data file.

    """

    with open(fname, 'r') as f:
        # Assignment expressions `:=` Python 3.8 and beyond only
        # (see https://peps.python.org/pep-0572/)
        while (chunk := np.fromfile(f, dtype=float, count=chunk_size)).size > 0:
            for item in chunk:
                yield item


# eager binary data reader (iterable) {{{2
def read_binary_eager(fname):
    """
    Eager binary data loader (iterable numpy array).

    Load data from a binary file specific to an application.  This loader is
    reading all content in the file eagerly.  It may consume a large amount of
    RAM on your system if the file is large.

    Parameters
    ----------
    fname : str
        Path to data file.

    Returns
    -------
    array_like
        NumPy array of data in file.

    """
    with open(fname, 'r') as f:
        return np.fromfile(f, dtype=float)


# lazy text data reader (generator) {{{2
def read_ascii_lazy(fname, sep=','):
    """
    Lazy ASCII data loader (generator).

    Alternative ASCII data loader for demonstration purpose.  Assume you are
    working with data sources that deliver the data in either binary form or
    ASCII text.  This additional data reader allows to read the ASCII version of
    the data sources.

    Parameters
    ----------
    fname : str
        Path to data file.

    Yields
    ------
    float
        One data element from the data file.
    """
    with open(fname, 'r') as f:
        # Assignment expressions `:=` Python 3.8 and beyond only
        # (see https://peps.python.org/pep-0572/)
        while (item := np.fromfile(f, count=1, sep=sep)).size > 0:
            yield item


# data generation {{{1
def gen_data(nelements, fname, sep=''):
    """
    Generate test data files.

    Parameters
    ----------
    nelements : int
        Number of random data elements.
    fname : str
        Path to data file.
    sep : str
        Data separator.  Binary file is generated if empty string.

    """
    x = np.random.rand(nelements)
    x.tofile(fname, sep=sep)


# main() {{{1
def main(args):
    # generate data {{{2
    if args.generate:
        n_floats = args.size * 1024 * 1024 // 8
        gen_data(n_floats, 'data.bin')  # random binary data
        gen_data(8, 'data.txt', sep=',')  # random text data

    # process data {{{2
    if os.path.isfile('data.bin') and os.path.isfile('data.txt'):
        sources = []

        # use an eager reader for demonstration, a large file will occupy a lot
        # of RAM
        if args.eager:
            sources.append(read_binary_eager('data.bin'))

        # performance demonstration is based on the lazy_binary data reader
        sources.append(read_binary_lazy('data.bin', args.chunk_size))

        # ASCII reader is just for additional demonstration that you can easily
        # treat different data sources in Python
        sources.append(read_ascii_lazy('data.txt'))

        # process all these sources
        result = process(*sources)
        print('Processed result:', result)


if __name__ == "__main__":
    args = parse_args()
    main(args)
