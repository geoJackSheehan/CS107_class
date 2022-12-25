#!/usr/bin/env python3
# File       : P4.py
# Description: Bank account revisited
# Copyright 2022 Harvard University. All Rights Reserved.
from enum import Enum


class Account(Enum):
    '''
    Simple enumeration
    See: https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use
    '''
    SAVINGS = 1
    CHECKING = 2


class BankAccount():
    '''Class for creating a bank account. Allows for deposits and withdrawals.'''

    def __init__(self, account_type: Account):
        # TODO: your code for b.)
        pass  # remove this line

    def __str__(self):
        # TODO: your code for b.)
        pass  # remove this line

    def get_type(self):
        # TODO: your code for b.)
        pass  # remove this line

    def get_balance(self):
        # TODO: your code for b.)
        pass  # remove this line

    def withdraw(self, amount: float):
        # TODO: your code for b.)
        pass  # remove this line

    def deposit(self, amount: float):
        # TODO: your code for b.)
        pass  # remove this line


class Customer():
    '''Class for a bank customer.'''

    def __init__(self, name):
        # TODO: your code for c.)
        pass  # remove this line

    def __str__(self):
        # TODO: your code for c.)
        pass  # remove this line

    def __len__(self):
        # TODO: your code for c.)
        pass  # remove this line

    def add_account(self, account_type: Account):
        # TODO: your code for c.)
        pass  # remove this line

    def get_balance(self, account_type: Account):
        # TODO: your code for c.)
        pass  # remove this line

    def deposit(self, account_type: Account, amount: float):
        # TODO: your code for c.)
        pass  # remove this line

    def withdraw(self, account_type: Account, amount: float):
        # TODO: your code for c.)
        pass  # remove this line


def ATMSession(user: Customer):
    # TODO: your code for d.)
    pass  # remove this line


def func(should_fail=True):
    if should_fail:
        raise ValueError("I have been told to fail here")


def test():
    print(type(Account))
    print(type(Account.SAVINGS))
    print(type(Account.SAVINGS.name))  # string representation of `SAVINGS`

    # test some basic logic
    try:
        assert Account.SAVINGS == Account.SAVINGS, (f"This is unexpected!")
    except AssertionError as e:
        print(e)  # it is unexpected that the above assertion is raised

    try:
        assert Account.CHECKING == Account.SAVINGS, (f"This is expected!")
    except AssertionError as e:
        print(e)  # it is expected that the above assertion is raised

    try:
        raise AssertionError(
            f"The `assert` keyword raises this exception when it evaluates to False"
        )
    except AssertionError as e:
        print(e)

    try:
        func()
    except ValueError as e:
        print(e)


    # TODO: your test code (optional)


if __name__ == "__main__":
    test()
