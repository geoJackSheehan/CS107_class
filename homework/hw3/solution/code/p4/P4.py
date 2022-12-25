#!/usr/bin/env python3
# vim: foldmethod=marker
#
# File       : P4.py
# Description: Bank account revisited (solution)
# Copyright 2022 Harvard University. All Rights Reserved.
from enum import Enum
from collections import namedtuple


class Account(Enum):
    '''
    Simple enumeration
    See: https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use
    '''
    SAVINGS = 1
    CHECKING = 2


# BankAccount {{{1
class BankAccount():
    '''Class for creating a bank account. Allows for deposits and withdrawals.'''

    def __init__(self, account_type: Account):
        self.type = account_type
        self.balance = 0.0

    def __str__(self):
        t = f"Type: {self.type.name}\n"
        b = f"\tBalance: {self.balance:.2f}"
        return t + b

    def get_type(self):
        return self.type

    def get_balance(self):
        return self.balance

    # If `raise` is used with other exception (should be meaningful) is also OK.
    def withdraw(self, amount: float):
        assert amount <= self.balance, (
            f"Amount {amount} is larger than current balance {self.balance}")
        assert amount >= 0, ("You cannot withdraw a negative amount")
        self.balance -= amount
        return self.balance

    # If `raise` is used with other exception (should be meaningful) is also OK.
    def deposit(self, amount: float):
        assert amount >= 0, ("You cannot deposit a negative amount")
        self.balance += amount
        return self.balance


# 1}}}
# Customer {{{1
class Customer():
    '''Class for a bank customer.'''

    def __init__(self, name):
        self.name = name
        self.accounts = {Account.SAVINGS: None, Account.CHECKING: None}

    def __str__(self):
        msg = f"Customer {self.name} has {len(self)} accounts"
        for account in self.accounts.values():
            if isinstance(account, BankAccount):
                msg += '\n' + account.__str__()
        return msg

    def __len__(self):
        count = 0
        for account in self.accounts.values():
            if isinstance(account, BankAccount):
                count += 1
        return count

    def _has_account(self, account_type: Account):
        '''Helper private method.  You are free to add additional code.'''
        if self.accounts.get(account_type, None) is None:
            return False
        return True

    def add_account(self, account_type: Account):
        if self._has_account(account_type):
            raise ValueError(
                f"{account_type.name} account for {self.name} already exists.")
        self.accounts[account_type] = BankAccount(account_type)

    def get_balance(self, account_type: Account):
        if not self._has_account(account_type):
            raise ValueError(
                f"{account_type.name} account for {self.name} does not exist.")
        return self.accounts[account_type].get_balance()

    def deposit(self, account_type: Account, amount: float):
        if not self._has_account(account_type):
            raise ValueError(
                f"{account_type.name} account for {self.name} does not exist.")
        return self.accounts[account_type].deposit(amount)

    def withdraw(self, account_type: Account, amount: float):
        if not self._has_account(account_type):
            raise ValueError(
                f"{account_type.name} account for {self.name} does not exist.")
        return self.accounts[account_type].withdraw(amount)


# 1}}}
# ATMSession {{{1
def ATMSession(user: Customer):
    assert isinstance(
        user, Customer
    ), 'ATM session user must be an instance of `Customer`'

    def session():
        CallbackEntry = namedtuple('CallbackEntry', ['name', 'callable'])
        callback_pool = {
            '1':
                CallbackEntry('Exit', None),
            '2':
                CallbackEntry(
                    'Create Account', lambda t: (
                        user.add_account(t),
                        print(f'Created New {t.name} Account')
                    )
                ),
            '3':
                CallbackEntry(
                    'Check Balance', lambda t: print(
                        'Current {} Balance: {:.2f}'.
                        format(t.name, user.get_balance(t))
                    )
                ),
            '4':
                CallbackEntry(
                    'Deposit', lambda t: print(
                        'New {} Balance: {:.2f}'.format(
                            t.name,
                            user.
                            deposit(t, float(input("Enter Deposit Amount: ")))
                        )
                    )
                ),
            '5':
                CallbackEntry(
                    'Withdraw', lambda t: print(
                        'New {} Balance: {:.2f}'.format(
                            t.name,
                            user.withdraw(
                                t, float(input('Enter Withdrawal Amount: '))
                            )
                        )
                    )
                )
        }

        def main_screen():
            msg = ''.join(
                [f'{k}) {e.name}\n' for k, e in callback_pool.items()]
            )
            code = input(msg + 'Enter Option: ')
            if code not in callback_pool:
                raise ValueError(f"Invalid option `{code}`")
            return code

        def account_type():
            code = input('1) Checking\n2) Savings\nChoose Account: ')
            if code == '1':
                return Account.CHECKING
            elif code == '2':
                return Account.SAVINGS
            else:
                raise ValueError(f"Invalid account option `{code}`")

        while True:  # main loop
            cID = main_screen()
            callback = callback_pool[cID].callable
            if callback is None:
                return 0
            account = account_type()
            callback(account)

    return session
# 1}}}
# Testing {{{1
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
# 1}}}


if __name__ == "__main__":
    test()
