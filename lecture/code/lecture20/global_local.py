#!/usr/bin/env python3
def f(x):
    l0 = x  # l0 and x are local names
    l1 = g  # g is a global name
    print(f'id(x) = {id(x)}')
    print(f'id(g) = {id(g)}')
    print(f'Local vars in f(x):  {locals()}')
    print(f'Global vars in f(x): {globals()}')


g = 42  # global name
# local and global scopes are identical in `__main__`:
# print(f'Local vars in `__main__`: {locals()}')
# print(f'Global vars in `__main__`: {globals()}')
f(g)
