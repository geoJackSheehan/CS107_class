#!/usr/bin/env python3
# File       : exercise_2.py
# Description: Linear autoencoder (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt

from exercise_1 import Layer


class LinearLayer(Layer):
    """Linear layer class.

    Class instances are created by passing a `shape` argument to the class
    initializer.
    """

    def __init__(self, shape):
        super(LinearLayer, self).__init__(shape, lambda x: x)

    def update(self, weights, biases):
        assert weights.size == self.w.size
        assert biases.size == self.b.size
        self.w = weights.reshape(self.w.shape)
        self.b = biases.reshape(self.b.shape)


class Autoencoder():
    """Autoencoder class with two linear layers."""

    def __init__(self, shape):
        self.l1 = LinearLayer(shape)  # encoder layer
        self.l2 = LinearLayer(shape[::-1])  # decoder layer

    @classmethod
    def from_pretrained(
        cls, encoder_weight, encoder_bias, decoder_weight, decoder_bias
    ):
        ae = cls(encoder_weight.shape)
        ae.l1.update(encoder_weight, encoder_bias)
        ae.l2.update(decoder_weight, decoder_bias)
        return ae

    def encode(self, inputs):
        return self.l1(inputs)  # base class `Layer` takes care of exceptions

    def decode(self, code):
        return self.l2(code)  # base class `Layer` takes care of exceptions


def main():
    data = np.load('data/autoencoder.npz')
    test_digit, enc_w, enc_b, dec_w, dec_b = [data[x] for x in data.files]
    ae = Autoencoder.from_pretrained(enc_w, enc_b, dec_w, dec_b)

    # reconstruct
    fig, ax = plt.subplots(len(test_digit), 2, sharex=True, sharey=True)
    for i, img in enumerate(test_digit):
        recon = ae.decode(ae.encode(img))  # encode/decode pass
        ax[i, 0].imshow(img.reshape(28, 28), cmap='gray_r')
        ax[i, 1].imshow(recon.reshape(28, 28), cmap='gray_r')
        for a in ax[i]:
            a.get_xaxis().set_visible(False)
            a.get_yaxis().set_visible(False)
    fig.savefig('test_digit.png', bbox_inches='tight')


if __name__ == "__main__":
    main()
