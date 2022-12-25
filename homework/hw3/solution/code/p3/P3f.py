#!/usr/bin/env python3
# File       : P3f.py
# Description: Model performance (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from P3c import LinearRegression
from P3d import RidgeRegression
from P3e import get_data


def main():
    # Load the data set
    X_train, X_test, y_train, y_test = get_data()

    # Train and score LinearRegression: not a function of \alpha -> R2 is
    # constant
    M1 = LinearRegression()
    M1.fit(X_train, y_train)
    tmp = M1.score(X_test, y_test)
    R2_M1 = []

    # Train and score RidgeRegression (\alpha = 0 -> OLS)
    alpha = np.linspace(0, 1, 100)
    M2 = RidgeRegression(0.0)
    R2_M2 = []
    for a in alpha:
        M2.set_params(alpha=a)
        M2.fit(X_train, y_train)
        R2_M1.append(tmp)
        R2_M2.append(M2.score(X_test, y_test))

    # Plot data
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(alpha, R2_M1, ls='-', lw=1.4, label='Ordinary Least Squares')
    ax.plot(alpha, R2_M2, ls='--', lw=1.4, label='Ridge Regression')
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$R^2$')
    ax.legend()
    fig.savefig('P3f.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
