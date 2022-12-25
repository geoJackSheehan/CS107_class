from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    name = "no name"
    x = 0
    y = 0
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y

    @classmethod
    def set_name(cls, name):
        cls.name = name

    def foo(self):
        return (self.x, self.y)

    @classmethod
    def class_foo(cls):
        return (cls.x, cls.y)

    @staticmethod
    def static_foo():
        return (x, y)

    @staticmethod
    def static_foo2(self):
        return (self.x, self.y)

    @staticmethod
    def static_foo3(cls):
        return (cls.x, cls.y)

    @staticmethod
    def change_mile_to_km(mile):
        return mile*1.6
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, passenger=0):
        super().__init__(x, y)
        self.passenger = passenger

        
s = Shuttle(10,0,3)
r = Rocket(1,2)

print(Rocket.name)
print(Shuttle.name)
print(s.name)
print(r.name)

print("change name") 
Shuttle.set_name("hello")
print(Rocket.name)
print(Shuttle.name)
print(s.name)
print(r.name)

print("start")
print(Rocket.class_foo())
print(Shuttle.class_foo())

print(r.class_foo())
print(s.class_foo())

print(r.foo())
print(s.foo())

print("static foo 2")
print(r.static_foo2(r))
print(s.static_foo2(s))
print(r.static_foo2(s))
print(s.static_foo2(r))

print(r.static_foo3(r))
print(s.static_foo3(s))

print(r.static_foo3(Rocket))
print(s.static_foo3(Shuttle))

print("static use")
print(r.change_mile_to_km(100))
print(Rocket.change_mile_to_km(100))
##error
#print(r.class_foo(Rocket))
#print(s.class_foo(Shuttle))

#print(r.static_foo())
#print(s.static_foo())