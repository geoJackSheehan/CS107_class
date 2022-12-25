#!/usr/bin/env python3
# File       : P3e.py
# Description: Model scores (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
from sklearn import datasets
from sklearn.model_selection import train_test_split

from P3c import LinearRegression
from P3d import RidgeRegression


def get_data(*, test_size=0.2, seed=42):
    dataset = datasets.fetch_california_housing()
    return train_test_split(dataset['data'],
                            dataset['target'],
                            test_size=test_size,
                            random_state=seed)

def main():
    # Load the data set
    X_train, X_test, y_train, y_test = get_data()

    # Train and score LinearRegression
    R = LinearRegression()
    R.fit(X_train, y_train)
    print("R^2 =", R.score(X_test, y_test), R)

    # Train and score RidgeRegression
    alpha = 0.1
    R = RidgeRegression(alpha)
    R.fit(X_train, y_train)
    print("R^2 =", R.score(X_test, y_test), R)


if __name__ == "__main__":
    main()
