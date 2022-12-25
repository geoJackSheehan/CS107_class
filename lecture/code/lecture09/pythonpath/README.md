# Setting up `PYTHONPATH` to point into custom Python code

You can use the `PYTHONPATH` environment variable to let the Python interpreter
know where to look for packages.  This is useful when you develop in order to
avoid installation cycles of your packages if you only want to test.

We have a CS107/AC207 test project called `cs107_package` in the parent
directory of this current directory.  When we are in the Python interpreter a
statement like `import cs107_package as cp` would fail because its location is
not in the search path of the interpreter.

You can solve this by adding the path to the Python package into the
`PYTHONPATH` environment variable.  See the `setup_pythonpath.sh` shell script
in this directory.  You can simply source it to add the new path.

```bash
source setup_pythonpath.sh
```

**NOTE:** you should avoid adding relative paths to environment variables like
`PATH` or `PYTHONPATH` as it will break you setup.  It is done here because it
will be easier for you to just test this out of the box.
