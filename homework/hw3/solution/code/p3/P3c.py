#!/usr/bin/env python3
# File       : P3c.py
# Description: Ordinary least squares linear regression (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np

from P3a import Regression as Base


class LinearRegression(Base):
    """Ordinary Least Squares regression"""

    def __init__(self):
        super(LinearRegression, self).__init__()

    def fit(self, X, y, standardize=False):
        if not standardize:
            # Account for intercept by adding column of ones
            X = np.append(np.ones((X.shape[0], 1)), X, axis=1)

            # Solution includes the intercept parameter (data is dimensional)
            beta = np.linalg.pinv(X.T @ X) @ X.T @ y

            # Set parameters
            self.params['intercept'] = beta[0]
            self.params['coeffs'] = beta[1:]
        else:
            # Standardize data
            ymean = np.mean(y)
            Xmean = np.mean(X, axis=0)
            scale = 1 / np.sqrt(np.sum((X - Xmean)**2, axis=0))
            Xs = (X - Xmean) * scale

            # Solution does not include intercept (\beta_0 = 0, data is
            # non-dimensional)
            beta = np.linalg.pinv(Xs.T @ Xs) @ Xs.T @ y

            # Set parameters (must be scaled back to correct units)
            beta *= scale
            self.params['intercept'] = ymean - Xmean @ beta
            self.params['coeffs'] = beta

    def __str__(self):
        return "LinearRegression"


def test():
    # Data: Draper and Smith, 'Applied Regression Analysis', 1998, Table 1.1
    X = np.array(
        ((35.3, ), (29.7, ), (30.8, ), (58.8, ), (61.4, ), (71.3, ), (74.4, ),
         (76.7, ), (70.7, ), (57.5, ), (46.4, ), (28.9, ), (28.1, ), (39.1, ),
         (46.8, ), (48.5, ), (59.3, ), (70.0, ), (70.0, ), (74.5, ), (72.1, ),
         (58.1, ), (44.6, ), (33.4, ), (28.6, )))
    y = np.array((10.98, 11.13, 12.51, 8.40, 9.27, 8.73, 6.36, 8.50, 7.82,
                  9.14, 8.24, 12.19, 11.88, 9.57, 10.94, 9.58, 10.09, 8.11,
                  6.83, 8.88, 7.68, 8.47, 8.86, 10.36, 11.08))
    sol = [13.623005, -0.079829]

    OLS = LinearRegression()
    OLS.fit(X, y)
    print("Raw data:")
    print(f"Error intercept: {(OLS.params['intercept'] - sol[0]) / sol[0]}")
    print(f"Error beta:      {(OLS.params['coeffs'][0] - sol[1]) / sol[1]}")
    OLS.fit(X, y, standardize=True)
    print("Standardized data:")
    print(f"Error intercept: {(OLS.params['intercept'] - sol[0]) / sol[0]}")
    print(f"Error beta:      {(OLS.params['coeffs'][0] - sol[1]) / sol[1]}")


if __name__ == "__main__":
    test()
