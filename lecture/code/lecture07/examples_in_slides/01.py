#!/usr/bin/env python3
def four():
    return 0x4

t = (1, 2.0, '3', four)
for item in t:
    print(type(item))
