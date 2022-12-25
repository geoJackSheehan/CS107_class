#!/usr/bin/env python3
import dis


def f_local_unbound(x):
    def closure(y):
        x -= y  # shadows `x` in the outer function
        return y

    return closure


def f_local_bound(x):
    def closure(y):
        y = x  # `x` does not shadow itself because it is not redefined in local scope
        return y

    return closure

def f_nonlocal(x):
    def closure(y):
        nonlocal x
        x -= y
        return x

    return closure


def f_global(x):
    def closure(y):
        global x
        x -= y
        return x

    return closure


def disassemble(f, val=0):
    c = f(val)
    # Tuple containing names of local variables referenced in nested functions
    print(f"{'Cell vars `' + f.__name__ + '`:':<32}{f.__code__.co_cellvars}")
    # Tuple containing names of local variables in outer function
    print(f"{'Local vars `' + f.__name__ + '`:':<32}{f.__code__.co_varnames}")
    # Tuple containing names of local variables in closure
    print(f"{'Local vars `' + c.__name__ + '`:':<32}{c.__code__.co_varnames}")

    print('Disassembly:')
    dis.dis(c)
    print('')


disassemble(f_local_unbound)
disassemble(f_local_bound)
disassemble(f_nonlocal)
disassemble(f_global)
