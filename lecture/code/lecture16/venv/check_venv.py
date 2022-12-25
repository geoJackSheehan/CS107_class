#!/usr/bin/env python3
# File       : check_venv.py
# Description: Check if you run in a virtual Python environment
# Copyright 2022 Harvard University. All Rights Reserved.
import sys

if __name__ == "__main__":
    print(sys.prefix)
    print(sys.base_prefix)
    try:
        assert sys.prefix == sys.base_prefix
    except AssertionError as e:
        print("--> Virtual Python environment is activated!")
