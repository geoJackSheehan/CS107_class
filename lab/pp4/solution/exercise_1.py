#!/usr/bin/env python3
# File       : exercise_1.py
# Description: Hidden layer for fully connected neural network (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np


def make_layer(shape, activation):
    """Create a neural network layer.

    Args:
        shape: A list with two elements for the number of layer inputs and the
          number of neural units in the layer.
        activation: An activation function object.

    Returns:
        A layer function object that takes arguments `inputs`, `weights` and
        `bias` for the layer.
    """

    def layer(inputs, weights, bias):
        assert inputs.size == shape[0], ('Layer input size is wrong')
        assert bias.size == shape[1], ('Layer bias size is wrong')
        assert weights.size == shape[0] * shape[1], (
            'Layer weights dimension is wrong'
        )
        return activation(np.dot(inputs, weights) + bias)

    return layer


def main():
    np.random.seed(101)  # use same seed for the tests

    n_input = 100  # number of input elements (e.g. MNIST: 28x28 pixel = 784)
    n_units = 3  # number of neural units (network architecture dependent)
    n_output = 1  # number of output elements (e.g. MNIST: 10 digits = 10)

    # network architecture
    shape1 = (n_input, n_units)  # shape of layer 1
    shape2 = (n_units, n_output)  # shape of layer 2 = output layer
    layer1 = make_layer(shape1, np.tanh)  # layer 1 instance
    layer2 = make_layer(shape2, np.tanh)  # layer 2 instance

    # random initialization of weights and bias
    w1 = np.random.uniform(-1.0, 1.0, size=shape1)
    b1 = np.random.normal(0.0, 0.1, size=shape1[1])
    w2 = np.random.uniform(-1.0, 1.0, size=shape2)
    b2 = np.random.normal(0.0, 0.1, size=shape2[1])

    # feed random input through network (forward pass)
    inp = np.random.uniform(0.0, 1.0, n_input).reshape(1, -1)  # input data
    out = layer2(layer1(inp, w1, b1), w2, b2)  # output
    print(out)

    # try some
    try:
        layer1(out, w1, b1)
    except AssertionError as e:
        print(e)

    try:
        layer1(inp, w2, b1)
    except AssertionError as e:
        print(e)

    try:
        layer1(inp, w1, b2)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
