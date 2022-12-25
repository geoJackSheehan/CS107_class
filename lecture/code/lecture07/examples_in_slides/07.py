#!/usr/bin/env python3
class Base():
    """Base class"""
    def __init__(self, a):
        self.a = a  # some data required in the base class

    def explain(self):
        print(f"Executing from base class: data=`{self.a}`")


class Derived(Base):
    """Derived class"""
    def __init__(self, a, b):
        super().__init__(a)  # properly initialize the base class
        self.b = b  # some data specific to the derived class

    def explain(self):
        # 1. Call the base class method first
        super().explain()
        # 2. Then do special work required for the derived class
        print(f"Executing from derived class: data=`{self.b}`")


a = "base class data"
b = "derived class data"
base = Base(a)
derived = Derived(a, b)

base.explain()
derived.explain()
print(Base.__mro__)
print(Derived.__mro__)
