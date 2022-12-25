#!/usr/bin/env python3
import time

def fast():
    time.sleep(0.5)

def slow():
    time.sleep(1)

def main():
    for i in range(5):
        fast()
    for i in range(3):
        slow()

if __name__ == "__main__":
    main()
