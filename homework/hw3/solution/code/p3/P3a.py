#!/usr/bin/env python3
# File       : P3a.py
# Description: Regression base class (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np

class Regression:
    """Regression base class"""

    def __init__(self):
        self.params = dict()

    def get_params(self):
        """Getter for parameters"""
        return self.params

    def set_params(self, **kwargs):
        """Setter for parameters"""
        self.params.update(kwargs)
        # raise NotImplementedError # also possible

    def fit(self, X, y):
        """Specific to derived class"""
        raise NotImplementedError

    def predict(self, X):
        """Predict using model equation"""
        return X @ self.params["coeffs"] + self.params["intercept"]

    def score(self, X, y):
        """R2 statistic"""
        y_hat = self.predict(X)  # prediction
        y_bar = np.mean(y)  # mean
        return 1 - np.sum((y - y_hat)**2) / np.sum((y - y_bar)**2)


def test():
    """Test function for your convenience.  We will not grade this code."""
    r = Regression()
    try:
        r.fit(None, None)
    except NotImplementedError:
        print("Caught `NotImplementedError`")


if __name__ == "__main__":
    test()
