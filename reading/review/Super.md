# What is super ?

```python
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls)+1]
```
MRO ( Method Resolution Order) represents the order of inheritance 
You can assume it is an order. 
```python
class A:
    def p(self):
        print('A')
class B(A):
    def p(self):
        super().p()
        print('B')
class C(B):
    def p(self):
        super().p()
        print('C')
class D(C):
    def p(self):
        super().p()
        print('D')
d = D()
d.p()
```

The MRO order is D->C->B->A  and the output is A B C D

### Case 1
```python
class A:
    def __init__(self):
        self.n = 2

    def plus(self, m):
        print('object is  {} from A'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def plus(self, m):
        print('object is  {} from B'.format(self))
        super().plus(m)
        self.n += 3

b = B()
b.plus(2)
print(b.n)
```

### Case 2
```python
class A:
    def __init__(self):
        self.n = 2

    def plus(self, m):
        print('object is  {} from A'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def plus(self, m):
        print('object is  {} from B'.format(self))
        A.plus(self,m)
        #self.plus(m) will throw an error
        self.n += 3

b = B()
b.plus(2)
print(b.n)
```

### Case 3
```python
class A:
    def __init__(self):
        self.n = 2

    def plus(self, m):
        print('object is  {} from A'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def plus(self, m):
        print('object is  {} from B'.format(self))
        # it will use the C.plus
        super().plus(m)
        self.n += 3

class C(A):
    def __init__(self):
        self.n = 4

    def plus(self, m):
        print('object is  {} from C'.format(self))
        super().plus(m)
        self.n += 4

#MRO order is D B C A
class D(B, C):
    def __init__(self):
        self.n = 5

    def plus(self, m):
        print('object is  {} from D'.format(self))
        # it will use the B.plus
        super().plus(m)
        self.n += 5

d = D()
d.plus(2)
print(d.n)
```
### Case 4
```python
class E(B, C):
    def __init__(self):
        self.n = 5

    def plus(self, m):
        print('object is  {} from E'.format(self))
        super(C,self).plus(m)
        #super(C,E).plus(self,m)
        self.n += 5

e = E()
e.plus(2)
print(e.n)
```
### Case 5
```python
class A:
    def spam(self):
        print('A.spam')
        super().spam()

class B:
    def spam(self):
        print('B.spam')

class C(A,B):
    pass
class D(B,A):
    pass
c = C()
c.spam() 
print("A.spam B.spam")

d = D()
d.spam()
print("B.spam")
```

## What is self ?

``` python
class A:
    def __init__(self):
        self.n = 2

    def plus(self, n):
        print("with self, ", self.n)
        print("with no self, ", n)
        self.n += n

a = A()
a.plus(7)
print(a.n)
```

ref
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
