#!/usr/bin/env python3
# File       : P3.py
# Description: Numerical approximation closures
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt


def approximate(f, eps):

    def first_order_FD(x):
        return (f(x + eps) - f(x)) / eps

    return first_order_FD


if __name__ == "__main__":
    aprx_v1 = approximate(np.log, 1.0e-1)
    aprx_v2 = approximate(np.log, 1.0e-7)
    aprx_v3 = approximate(np.log, 1.0e-15)

    x = np.linspace(.2, .4, 20)

    # yapf: disable
    plt.plot(x, aprx_v1(x), ls='none', marker='o', label=r'$\varepsilon=1\times 10^{-1}$')
    plt.plot(x, aprx_v2(x), ls='none', marker='^', label=r'$\varepsilon=1\times 10^{-7}$')
    plt.plot(x, aprx_v3(x), ls='none', marker='s', label=r'$\varepsilon=1\times 10^{-15}$')
    # yapf: enable
    plt.plot(x, 1 / x, ls='--', color='k', lw=1.5, label='Exact', zorder=-10)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$df/dx$')
    plt.legend()
    plt.savefig('P3.png', dpi=300, bbox_inches='tight')

    print(
        """Answer to Q-i:
    * The parameter eps=1.0e-7 performs best.
    * For eps too small round-off errors due to limited machine precision
    become the dominant source or error.
    * For $\epsilon$ too large the numerical approximation (the algorithm)
    becomes inaccurate.
    """
    )

    print(
        """Answer to Q-ii:
    Automatic differentiation evaluates derivatives exact up to machine
    precision without relying on numerical approximation schemes.
    """
    )
