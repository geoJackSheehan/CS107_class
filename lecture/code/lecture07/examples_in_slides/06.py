#!/usr/bin/env python3
class Animal():
    """Base class for animals"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # class method, note how `self` is passed as argument
    def speak(self):
        """Sounds animals can make"""
        raise NotImplementedError


class Dog(Animal):  # Dog is a derived class, it inherits from Animal
    """Dog is a derived Animal class"""
    def speak(self):
        """Special sounds dogs make"""
        return "Woof"

    def my_id(self):
        print(id(self))


class Cat(Animal):  # Cat is a derived class, it inherits from Animal
    """Cat is a derived Animal class"""
    def __init__(self, name, age):
        self.name = f"A very special cat: {name}"  # cats have a special name string

    def speak(self):
        """Special sounds cats make"""
        return "Meow"


dog = Dog("Snoopy", 6)
cat = Cat("Kitty", 4)
print(dog.speak())
print(cat.speak())

if isinstance(dog, Animal):
    print(f"dog ({id(dog)}) is an instance of Animal")
if isinstance(cat, Animal):
    print(f"cat ({id(cat)}) is an instance of Animal")
