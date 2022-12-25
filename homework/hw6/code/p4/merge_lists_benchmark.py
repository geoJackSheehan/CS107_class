#!/usr/bin/env python3
# File       : merge_lists_benchmark.py
# Description: Benchmark to test priority queue implementations based on list
#              merge example
# Copyright 2022 Harvard University. All Rights Reserved.
import time
from random import sample
import numpy as np

def benchmark(n_lists, queue_type, *, n_samples=5, list_length=20, debug=False):
    """
    Run benchmark for merging a number of sorted lists using a priority queue.

    Parameters
    ----------
    n_lists : int or array of int
        Number of lists to be used for benchmark run.  Can be an array of
        integers for multiple runs.
    queue_type : PriorityQueue
        Type of priority queue to be used in benchmark.
    n_samples : int
        Number of sample runs per case to compute average and standard deviation
        of runtime.
    list_length : int
        Number of elements per list.
    debug : bool
        Print lists if `True`.

    Returns
    -------
    List float
        List of floats with mean runtime in milli-seconds for each list merge
        defined by `n_lists`.

    """

    def merge_sorted_lists(queue_type, n, list_length, debug=False):
        # generate n random lists of list_length
        lists = [
            sorted(sample(range(-list_length, list_length, 1), list_length))
            for _ in range(n)
        ]
        if debug:
            for l in lists:
                print('Sample list:', l)

        # queue to use for list merging
        queue = queue_type(len(lists))
        for i, l in enumerate(lists):
            queue.put((l.pop(0), i))

        # merge sorted lists together
        merged_list = []
        while len(queue) > 0:
            val, i = queue.get()
            merged_list.append(val)
            feed = lists[i]
            if feed:
                queue.put((feed.pop(0), i))
        return merged_list

    results = []
    if isinstance(n_lists, int):
        n_lists = [n_lists]
    for n in n_lists:
        measurements = []
        for _ in range(n_samples):
            t0 = time.time()
            res = merge_sorted_lists(queue_type, n, list_length, debug)
            t1 = time.time()
            if debug:
                print('Merged list:', res)
            measurements.append((t1 - t0) * 1000.0)  # milli-seconds
        results.append(np.mean(measurements))
    return results
