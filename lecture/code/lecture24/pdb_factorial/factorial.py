#!/usr/bin/env python3


def factorial(x):
    if x > 1:
        return x * factorial(x - 1)  # recursive call
    return 1


def main():
    return factorial(5)


if __name__ == "__main__":
    main()
