#!/usr/bin/env python3
# File       : P5a.py
# Description: Analogue clock using Python closure.
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Define your closure here
def clock_hand(r):  # do not change this function name and parameter list
    """Function for a clock hand

    Parameters
    ----------
    r : float
        Length of the clock hand

    Returns
    -------
    callable
        Returns the callable closure function.  The returned function takes a
        single floating point argument `theta` and returns a list-like object
        (x, y) for the `x` and `y` Cartesian coordinates of the clock hand
        position.
    """
    # TODO: implement the closure.  Replace the `lambda theta: (0, 0)`
    # expression below with the name of your implemented closure.

    return lambda theta: (0, 0)  # replace the lambda with your closure


t = dt.datetime.now()
h = t.hour
m = t.minute
s = t.second

# Specify the length of hour, minute and second hands

# Calculate theta in degrees for each hand based on current time

# hour = clock_hand(r_h)
# x_h, y_h = hour(theta_h)

# Plot the clock
