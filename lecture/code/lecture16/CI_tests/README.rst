Test project for continuous integration and testing
===================================================

Test project continuation lecture 14/15: adding CI and Python ``unittest`` and
``pytest`` tests.


.. code:: console

    .
    ├── docs
    │   ├── conf.py
    │   ├── index.rst
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── cs107_package
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── subpkg_1
    │       │   ├── __init__.py
    │       │   ├── module_1.py
    │       │   └── module_2.py
    │       └── subpkg_2
    │           ├── __init__.py
    │           ├── module_3.py
    │           ├── module_4.py
    │           └── module_5.py
    └── tests
        ├── run_coverage.sh
        ├── run_tests.sh
        └── subpkg_1
            ├── test_module_1.py
            └── test_module_2.py
