#!/usr/bin/env python3
# File       : P4b.py
# Description: Bank withdrawal (solution)
# Copyright 2022 Harvard University. All Rights Reserved.


def make_withdraw(balance):

    def withdraw(amount):
        if amount > balance:
            raise ValueError(f"Amount of {amount} exceeds balance {balance}.")
        else:
            balance -= amount
            return balance

    return withdraw


if __name__ == "__main__":
    initial_balance = 1000.0
    withdraw = [100.0, 100.0, 2000.0]

    print("""The variable `balance` has never been defined (bound to a name) in
        the closure.  The name resolution is not beyond the function definition
        and therefore Python complains that the variable balance has not been
        defined at the point of assignment.""")

    wd = make_withdraw(initial_balance)
    for i, w in enumerate(withdraw):
        try:
            print(f"Withdraw {i+1}: amount is {w} --> new balance is {wd(w)}")
        except ValueError as e:
            print(e)
