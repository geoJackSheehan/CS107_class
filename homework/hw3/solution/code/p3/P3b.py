#!/usr/bin/env python3
# File       : P3b.py
# Description: Import parts of a module (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
from P3a import Regression as Base

if __name__ == "__main__":
    r = Base()  # create instance
    print(dir(r))  # print attributes of instance (this includes `params`)
