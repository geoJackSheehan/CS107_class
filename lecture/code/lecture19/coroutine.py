#!/usr/bin/env python3
# File       : coroutine.py
# Description: Simple coroutine example
# Copyright 2022 Harvard University. All Rights Reserved.
from inspect import getgeneratorstate


def coroutine():
    ncalls = 0
    while True:
        x = yield ncalls
        ncalls += 1
        print(f'coroutine(): {x} (call id: {ncalls})')


def main():
    c = coroutine()
    print(getgeneratorstate(c))
    next(c)  # prime the coroutine; next() returns 0 here
    print(getgeneratorstate(c))

    c.send('CS107')
    print('main(): control back in main function')
    n_call = c.send('AC207')
    print(f'main(): called coroutine() {n_call} times')

    c.close()
    print(getgeneratorstate(c))


if __name__ == "__main__":
    main()
