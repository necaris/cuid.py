# cuid.py [![Build Status](https://travis-ci.org/necaris/cuid.py.svg)](https://travis-ci.org/necaris/cuid.py)

Implementation of https://github.com/ericelliott/cuid in Python.

A `cuid` is a portable and sequentially-ordered unique identifier designed for horizontal scalability and speed -- this version is ported from the reference implementation in Javascript.

Tested on CPython 2.7 and 3.4 as well as PyPy.

Rough benchmarks on my machine (2.2GHz i7, 2012 Macbook Pro):
- Python 3.4: 19.38μs per cuid
- Python 2.7: 17.58μs per cuid
- PyPy 2.6: 4.28μs per cuid

*Note*: For now, this has no dependencies outside the standard library -- in time this may change, to provide better random numbers and / or performance.
