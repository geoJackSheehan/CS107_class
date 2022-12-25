#!/usr/bin/env python3
# File       : P3d.py
# Description: Ridge regression (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np

from P3c import LinearRegression


class RidgeRegression(LinearRegression):
    """Ridge regression"""

    def __init__(self, alpha=0.1):
        super(RidgeRegression, self).__init__()
        self.params["alpha"] = alpha

    def fit(self, X, y, standardize=False):
        if not standardize:
            # Scale the data for fitting: scaling is necessary to ensure the
            # units are correct!  If X has units U and y has units V, then we
            # must make sure that coefficients beta have units V/U because when
            # we predict we form the products beta * X to predict values y.
            Xmean = np.mean(X, axis=0)
            scale = 1 / np.sqrt(np.sum((X - Xmean)**2, axis=0))
            Xs = X * scale

            # Account for intercept by adding column of ones to scaled data
            Xs = np.append(np.ones((Xs.shape[0], 1)), Xs, axis=1)
            G = self.params['alpha'] * np.identity(Xs.shape[1])  # Gamma
            G[0, 0] = 0  # penalizing the intercept will not give correct result
            beta = np.linalg.pinv(Xs.T @ Xs + G.T @ G) @ Xs.T @ y

            # Set parameters (coefficients must be scaled back for correct units)
            self.params['intercept'] = beta[0]
            self.params['coeffs'] = beta[1:] * scale
        else:
            # Standardize data
            ymean = np.mean(y)
            Xmean = np.mean(X, axis=0)
            scale = 1 / np.sqrt(np.sum((X - Xmean)**2, axis=0))
            Xs = (X - Xmean) * scale

            # Solution does not include intercept (\beta_0 = 0, data is
            # non-dimensional, \alpha has no units)
            G = self.params['alpha'] * np.identity(Xs.shape[1])  # Gamma
            beta = np.linalg.pinv(Xs.T @ Xs + G.T @ G) @ Xs.T @ y

            # Set parameters (must be scaled back to correct units)
            beta *= scale
            self.params['intercept'] = ymean - Xmean @ beta
            self.params['coeffs'] = beta

    def __str__(self):
        return "RidgeRegression"


def test():
    # Data: Hilt & Seegrist, 1977. https://srs.fs.usda.gov/pubs/19260
    X = np.array((
        (11, 11, 11),
        (14, 15, 11),
        (17, 18, 20),
        (17, 17, 18),
        (18, 19, 18),
        (18, 18, 19),
        (19, 18, 20),
        (20, 21, 21),
        (23, 24, 25),
        (25, 25, 24),
    ))
    y = np.array((
        223,
        223,
        292,
        270,
        285,
        304,
        311,
        314,
        328,
        340,
    ))
    alpha = np.sqrt(0.2)

    print("Expected: y = 132.5 + 2.870 X_1 + 1.650 X_2 + 3.934 X_3")

    R = RidgeRegression(alpha)
    R.fit(X, y)
    print("Raw data (scaled only):")
    print("Model:    y = {:.1f} + {:.3f} X_1 + {:.3f} X_2 + {:.3f} X_3".format(
        R.params['intercept'], *R.params['coeffs']))
    R.fit(X, y, standardize=True)
    print("Standardized data:")
    print("Model:    y = {:.1f} + {:.3f} X_1 + {:.3f} X_2 + {:.3f} X_3".format(
        R.params['intercept'], *R.params['coeffs']))


if __name__ == "__main__":
    test()
