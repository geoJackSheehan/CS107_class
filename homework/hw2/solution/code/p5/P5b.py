#!/usr/bin/env python3
# File       : P5b.py
# Description: Analogue clock using Python closure animation (solution).
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

from P5a import *

fig, ax = plt.subplots(figsize=(3, 3))
for i in range(100):
    ax.clear()

    t = dt.datetime.now()
    h = t.hour
    m = t.minute
    s = t.second

    # Calculate theta in degrees for each hand
    if (h > 12):
        h -= 12  # convert to twelve-hour clock
    theta_h = 90.0 - 30.0 * h - 0.5 * m
    theta_m = 90.0 - 6.0 * m
    theta_s = 90.0 - 6.0 * s

    x_h, y_h = hour(theta_h)
    x_m, y_m = minute(theta_m)
    x_s, y_s = second(theta_s)

    # Plot the clock
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title(f"The time is {h:02d}:{m:02d}:{s:02d}")
    ax.plot([0.0, x_h], [0.0, y_h], lw=4, c='k')
    ax.plot([0.0, x_m], [0.0, y_m], lw=3, c='k')
    ax.plot([0.0, x_s], [0.0, y_s], lw=1, c='k')

    L = max(r_h, r_m, r_s) * 1.05
    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    L = max(r_h, r_m, r_s)
    for tick in range(1, 13, 1):
        theta = np.pi * tick / 6
        x = L * np.sin(theta)
        y = L * np.cos(theta)
        ax.text(x, y, f"{tick}", ha='center', va='center', c='k')

    fig.canvas.draw()
    plt.pause(0.1)
