# Scope

Using the LEGB Rule for Python Scope

Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. The letters in LEGB stand for Local, Enclosing(nonlocal), Global, and Built-in. 

https://realpython.com/python-scope-legb-rule/#:~:text=Enclosing%20(or%20nonlocal)%20scope%20is,define%20in%20the%20enclosing%20function.

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

In the function scope_test, "spam" points to "test spam"

### (1)local 

a. It will run the function do_local and read a local variable "spam" with value "local spam"

b. After spam = "local spam" finishes，the whole do_local function is done and the related space is deleted
at this point, the variable local variable (the meaning of local refers to variables within do_local )spam is deleted and it doesn't change the value of spam in scope_test()

c. Print the value of spam (this is the spam in the scope_test())

### (2)nonlocal 

a. It will run the do_nonlocal()

In this program, it declares a nonlocal variable and assigns this variable a value "nonlocal spam". 

b. print the spam value

c. After the nonlocal declaration, the scope of spam is neither inside do_nonlocal() nor the entire module, but the function scope_test that is closest to do_nonlocal and one layer outside.

### (3)global 

In this module, the value of spam is set to "global spam" but the value of the spam in the scope_test() is still "nonlocal spam"


## A Complex Example
```diff
+ What's the output?
```

```python
flist = []

for i in range(3):
	def func(x):
		print("inside func ", x*i, " x is ",x, " i is ", i)
		return x*i 

	flist.append(func)

for f in flist:

	print(f(2))
```

```python

flist = []

for i in range(3):
	def makefun(i):
		def func(x):
			#print("inside func ", x*i, " x is ",x, " i is ", i)
			return x*i 
		return func

	flist.append(makefun(i))

for f in flist:

	print(f(2))
```
