#!/usr/bin/env python3
# File       : exercise_1.py
# Description: Hidden layer class for fully connected neural network (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np


class Layer():
    """Neural network layer class.

    Class instances are created by passing a `shape` and `activation` argument
    to the class initializer.
    """

    def __init__(self, shape, activation):
        self.phi = activation
        self.w = np.random.uniform(-1.0, 1.0, size=shape)
        self.b = np.random.normal(0.0, 0.1, size=shape[1])

    def __call__(self, inputs):
        """Evaluate the layer.

        Args:
            inputs: input values fed into the layer.
        """
        assert inputs.size == self.w.shape[0], ('Layer input size is wrong')
        return self.phi(np.dot(inputs, self.w) + self.b)

    def __repr__(self):
        name = type(self).__name__
        return f"{name}(shape={self.w.shape}, activation={repr(self.phi)})"

    def __str__(self):
        h = f"Layer:\n"
        i = f"\tinputs     = {self.w.shape[0]}\n"
        o = f"\toutputs    = {self.w.shape[1]}\n"
        a = f"\tactivation = {self.phi.__name__}"
        return h + i + o + a


def main():
    s1 = (100, 3)
    l1 = Layer(s1, np.tanh)
    inp = np.random.uniform(0.0, 1.0, s1[0]).reshape(1, -1)
    out = l1(inp)
    print(out)
    print(repr(l1))
    print(str(l1))

    # try some
    try:
        print(l1(inp[0, :10]))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
