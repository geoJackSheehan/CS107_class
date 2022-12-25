#!/usr/bin/env python3
# File       : jacobian.py
# Description: Compute the Jacobian of f(x) symbolically
# Copyright 2021 Harvard University. All Rights Reserved.
import sympy as sym

x = sym.symbols('x')  # define the symbolic variable
sym.init_printing(use_unicode=True)  # for pretty terminal printing

f = x - sym.exp(-2 * sym.sin(4 * x)**2)  # our function f(x)
J = sym.diff(f, x)  # compute the derivative w/r/t x
print(J)
