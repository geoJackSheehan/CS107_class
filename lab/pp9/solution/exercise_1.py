# File       : exercise_1.py
# Description: PP9: Fibonacci class with iterator
# Copyright 2022 Harvard University. All Rights Reserved.


class FibonacciIterator:
    """Fibonacci recurrence iterator.

    The class defines three dunder methods: __init__, __next__ and __iter__.

    __init__: Takes the number of Fibonacci numbers to be computed (including
    the initial two numbers) as an argument and initializes the first two
    numbers in the recurrence.

    __next__: Returns F_{n-2} in equation (1) of the work sheet and advances the
    recurrence.  If there are no more terms left, a `StopIteration` exception
    must be raised.

    __iter__: Returns the iterator.

    Example:

    >>> fib_iter = FibonacciIterator(4)
    >>> list(fib_iter)
    [0, 1, 1, 2]

    """

    def __init__(self, N):
        assert N > 1
        self.N = N
        self.F0 = 0
        self.F1 = 1

    def __next__(self):
        if self.N < 1:
            raise StopIteration

        self.N -= 1
        ret = self.F0
        self.F0, self.F1 = self.F1, self.F0 + self.F1
        return ret

    def __iter__(self):
        return self


class Fibonacci:

    def __init__(self, N):
        self.N = N

    def __iter__(self):
        return FibonacciIterator(self.N)


if __name__ == "__main__":
    fib = Fibonacci(12)
    print(iter(fib))
    print(len(list((fib))))  # 12
    print(list(fib))  # the list() built-in assumes the object `fib` is iterable
