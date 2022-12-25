---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Introductory Python


The main topic for today's lecture is Python and some of it's basic
functionality.  We will cover the basics of 

* using Python as a calculator
* `print` statements
* the list concept
* opening and reading from files
* dictionaries
* strings

I will show you some very basic examples and you will put them all together in a
small script for your exercise.  The exercise is displayed at the top of this
notebook.  If you already know how to do it, then just write up your script now.
However, you may need some guidance.  You will find such guidance throughout the
rest of the notebook.


## Important, Useful Libraries


You should always try to use existing technologies to accomplish your goals
whenever possible.  For example, don't write your own function to compute the
square root of a number.  That would be really hard and your implementation
would most likely not be very efficient.  Instead, use built-in functionality or
functionality from a nice library such as `numpy`
([NUMericalPYthon](http://www.numpy.org/)).

> NumPy is the fundamental package for scientific computing with Python. It
> contains among other things:
>
> * a powerful N-dimensional array object 
> * sophisticated (broadcasting) functions 
> * tools for integrating C/C++ and Fortran code 
> * useful linear algebra, Fourier transform, and random number capabilities 
>
> Besides its obvious scientific uses, NumPy can also be used as an efficient
> multi-dimensional container of generic data. Arbitrary data-types can be
> defined. This allows NumPy to seamlessly and speedily integrate with a wide
> variety of databases.

To import libraries into your Python application, do the following:

```python
# The %... is an iPython thing, and is not part of the Python language.
# In this case we're just telling the plotting library to draw things on
# the notebook, instead of on a separate window.
%matplotlib inline 
# the line above prepares IPython notebook for working with matplotlib

import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
```

The way to understand these imports is as follows: _import the library `library`
with the alias `lib`_ where `library` could be `numpy` or `matplotlib` or
whatever you want and `lib` is the alias used to refer to that library in our
code.  Using this flow, we can call methods like `plt.plot()` instead of
`matplotlib.pyplot.plot()`.  It makes life easier.


**NOTE:** It is not necessary to import _all_ of these libraries all of the
time.  You should only import the ones you really need.  I listed a bunch above
to give you a sampling of what's available.

**NOTE:** DO NOT include `%matplotlib inline` in your Python scripts unless
you're working in the Jupyter notebook.


At the end of this course, someone should be able to `import
your_kinetics_library` to use the kinetics library that you are about to start
writing.


## The Very Basics


We'll fly through this part because you should already know it.  If you don't
understand something, please Google it and/or refer to the [Python
Tutorial](https://docs.python.org/3/tutorial/).  I do not want to recreate the
Python tutorial here; instead, I'll just summarize a few important ideas from
Python.  We'll give more details a little later on how some of these language
features work.

Another very helpful resource that explains the basics below (and few additional
topics) can be found here:
[https://learnxinyminutes.com/docs/python/](https://learnxinyminutes.com/docs/python/).


### Calculating


We can tell the type of a number or variable by using the `type` function.

```python
type(3), type(3.0)
```

Remember, every variable in python gets a type. Python is a strongly typed
language. It is also a dynamic language, in the sense that types are assigned at
run-time, rather then "compile" time, as in a language like C. This makes it
slower, as the way data is stored cannot be initially optimal, as when the
program starts, you dont know what that variable will point to.


All the usual calculations can be done in Python.

```python
2.0 + 4.0 # Adding two floats
```

```python
2 + 4     # Adding two ints
```

```python
1.0 / 3.0 # Dividing two floats
```

```python
1 / 3     # Dividing two ints
```

Note that in Python 2, the division of two ints would not be interpreted as a
float; it is integer division.  This is new in Python 3!  Now, if you want
integer division you have to use the `//` operator.

```python
1 // 3    # Integer division
```

```python
2**5      # Powers
```

```python
3 * 5     # Multiplication
```

#### More advanced operations

We can use `numpy` to do some more advanced operations.

```python
np.pi * np.exp(2.0) + np.tanh(1.0) - np.sqrt(100.0)
```

Notice that I am always writing my floats with a decimal point.  You don't
really need to do that in Python because Python will automatically convert
between types.  For example:

```python
type(np.pi * np.exp(2.0) + np.tanh(1.0) - np.sqrt(100.0)), type(np.pi * np.exp(2) + np.tanh(1) - np.sqrt(100))
```

However, I like to make the types as explicit as I can so there's no confusion.


### `print`


The `print` function is the basic way to write information out to the screen.  I
will briefly review the new form of the `print` function.  In Python 2, `print`
was a `statement` rather than a `function`.

```python
print('Good morning!  Today we are doing Python!')                                  # Basic print
print(3.0)                                                                          # Print a float
print('{} is a nice, trancendental number'.format(np.pi))                           # Print just one number
print('{} is nice and so is {}'.format('Eric', 'Sarah'))                            # Print with two arguments
print('{0:20.16f}...: it goes on forever but {1} is just an int.'.format(np.pi, 3)) # Print with formatting in argument 0
```

Here are some additional resources for the `print` function and formatting:
* [7. Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
* [Formatted Output](https://www.python-course.eu/python3_formatted_output.php)
* [`Print` function](https://docs.python.org/3/library/functions.html#print)


### Variables


We'll have more to say about variables in Python later.  For now, here's how you
store them syntactically:

```python
a = 1.0
b = -1.0
c = -1.0
x = (1.0 + np.sqrt(5.0)) / 2.0
val = a * x**2.0 + b * x + c
print('{0}x^2 + {1}x + {2} = {3}'.format(a, b, c, val))
```

Python has this nice feature where you can assign more than one variable all on
one line.  It's called the multiple assignment statement.

```python
a, b, c = 1.0, -1.0, -1.0
x = (1.0 + np.sqrt(5.0)) / 2.0
val = a * x**2.0 + b * x + c
print('{0}x^2 + {1}x + {2} = {3}'.format(a, b, c, val))
```

Looks a little cleaner now.


### Lists and `for` loops


Lists are central to Python.  Many things behave like lists.  For now, we'll
just look at how to create them and do basic operations with them.  I will not
go through all the details.  Please refer to
[Lists](https://docs.python.org/3/tutorial/introduction.html#lists) for
additional examples.

```python
primes = [2, 3, 5, 7, 11, 13]     # A list of primes
more_primes = primes + [17, 19]   # List concatentation
print('First few primes are: {primes}'.format(primes=primes))
print('Here are the primes up to the number 20: {}'.format(more_primes))
```

Notice that Python knows that type of `primes`.

```python
print('primes is of type {}'.format(type(primes)))
```

The `len` function can provide the number of elements in the list.

```python
print('There are {} prime numbers less than or equal to 20.'.format(len(primes)))
```

Now that we know what a list is, we can discuss `for` loops in Python.  The
`for` loop iterates over an iterator such as a list.  For example:

```python
for p in more_primes:
    print(p)
```

A useful iterator (but not a list!) is the `range` function.

```python
print(range(10))
print(type(range(10)))
```

It's not a list anymore (it used to be in Python 2) and therefore can't be
sliced like a list can (see below).  Still, you can use it in `for` loops which
is where it finds most of its use.

```python
for n in range(10):
    print(n)
```

There is something called a _list comprehension_ in Python.  List comprehensions
are just a way to transform one list into another list.

```python
not_all_primes = [p // 3 for p in more_primes]
print('The new list is {}'.format(not_all_primes))
```

We can also count the number of each element in the list.  There are a number of
ways of doing this, but one convenient way is to use the `collections` library.

```python
import collections
how_many = collections.Counter(not_all_primes)
print(how_many)
print(type(how_many))
```

We see that there are 2 ones, 1 two, 1 three, etc.

We can even find the most common element of the list and how many occurrences of
it there are and return the result as a list.

```python
how_many_list = how_many.most_common()
print(how_many_list)
print(type(how_many_list))
```

We see that the result is a list of tuples with the most common element of our
original list (`not_all_primes`) displayed first.  We want the most common
element of our original list, so we just access the first element using a simple
index.

```python
most_common = how_many_list[0]
print(most_common)
print(type(most_common))
```

We're almost there.  We recall the first element of this tuple is the value from
our original list and the second element in the tuple is its frequency.  We're
finally ready to get our result!

```python
print('The number {} is the most common value in our list.'.format(most_common[0]))
print('It occurs {} times.'.format(most_common[1]))
```

List indexing is also very important.  It can also do much more than what we did
above.

```python
print(primes[2])   # print the 3rd entry 
print(primes[2:5]) # print the 3rd to 5th entries
print(primes[-1])  # print the last entry
print(primes[-3:]) # print the three entries
```

Other types of slices and indexing can be done as well.  I leave it to you to
look this up as you need it.  It is a **very** useful thing to know.


Two convenient built-in functions are `enumerate` and `zip`.  You may find
various uses for them.

* `enumerate` gives a representation of a list of tuples with each tuple of the
  form `(index, value)`.  This provides an easy way to access the `index` of the
  value in the `list`.
* `zip` takes elements from each list and puts them together into a
  representation of a list of tuples.  This provides a nice way to aggregate
  lists.


We'll make two lists for the following examples:

```python
species = ['H2', 'O2', 'OH', 'H2O', 'H2O2']
species_names = ['Hydrogen', 'Oxygen', 'Hydroxyl', 'Water', 'Hydrogen Peroxide']
```

#### `enumerate` example

```python
print(enumerate(species)) 
```

Notice that `enumerate()` just returns an iterator object.  To actually see
what's in the iterator object, we need to convert the iterator object to a list

```python
print(list(enumerate(species)))
```

We see that we have a list of tuples (in the form `(index, value)` where `index`
starts from 0).  Here's just one way that this might be used:

```python
for i, s in enumerate(species):
    print('{species} is species {ind}'.format(species=s, ind=i+1))
```

What happened is that the `for` loop iterated over the iterable (here
`enumerate`).  The first index in the `for` loop corresponds to the first entry
in the `enumerate` tuple and the second index in the `for` loop corresponds to
the second entry in the `enumerate` tuple.


#### `zip` example


Let's see how `zip` works.  We'll aggregate the `species` and `species_names`
lists.

```python
print(zip(species, species_names))
print(list(zip(species, species_names)))
```

```python
for s, name in zip(species, species_names):
    print('{specie} is called {name}'.format(specie=s, name=name))
```

We see that this worked in a similar way to `enumerate`.


Finally, you will sometimes see `enumerate` and `zip` used together.

```python
for n, (s, name) in enumerate(zip(species, species_names), 1):
    print('Species {ind} is {specie} and it is called {name}.'.format(ind=n, specie=s, name=name))
```

### Opening Files


There are a variety of ways to open files in Python.  We'll see a bunch as the
semester progresses.  Today, we'll focus on opening and reading text files.

```python
species_file = open("species.txt") # Open the file
species_text = species_file.read() # Read the lines of the file
species_tokens = species_text.split() # Split the string and separate based on white spaces
species_file.close()               # Close the file!
```

```python
print(species_tokens)
print(type(species_tokens))
```

Notice that we get a list of strings.


Here's a better way to open a file.  The `close` operation is handled
automatically for us.

```python
with open('species.txt') as species_file:
    species_text = species_file.read()
    species_tokens = species_text.split()
```

### Dictionaries


Dictionaries are extremely important in Python.  For particular details on
dictionaries refer to
[Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
From that tutorial we have a few comments on dictionaries:

> Unlike sequences, which are indexed by a range of numbers, dictionaries are
> indexed by keys, which can be any immutable type; strings and numbers can
> always be keys.
>
> It is best to think of a dictionary as an unordered set of key: value pairs,
> with the requirement that the keys are unique (within one dictionary). A pair
> of braces creates an empty dictionary: {}. Placing a comma-separated list of
> key:value pairs within the braces adds initial key:value pairs to the
> dictionary; this is also the way dictionaries are written on output.
>
> The main operations on a dictionary are storing a value with some key and
> extracting the value given the key.


Let's create a chemical species dictionary.

```python
species_dict = {'H2':'Hydrogen', 'O2':'Oxygen', 'OH':'Hydroxyl', 'H2O':'Water', 'H2O2':'Hydrogen Peroxide'}
print(species_dict)
```

The entries to the left of the colon are the keys and the entries to the right
of the colon are the values.  To access a value we just reference the key.

```python
print(species_dict['H2'])
```

Pretty cool!

Suppose we want to add another species to our dictionary.  No problem!

```python
species_dict['H'] = 'Atomic Hydrogen'
print(species_dict)
print(species_dict['H'])
```

Why should we use dictionaries at all?  Clearly they're very convenient.  But
they're also fast.  See [indexnext |previous |How to Think Like a Computer
Scientist: Learning with Python 3: 20.
Dictionaries](http://openbookproject.net/thinkcs/python/english3e/dictionaries.html)
for a decent explanation.
