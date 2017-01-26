# cuid.py [![Build Status](https://travis-ci.org/necaris/cuid.py.svg)](https://travis-ci.org/necaris/cuid.py)

Implementation of https://github.com/ericelliott/cuid in Python.

A `cuid` is a portable and sequentially-ordered unique identifier designed for
horizontal scalability and speed -- this version is ported from the reference
implementation in Javascript.

Tested on CPython 2.7-3.6 as well as PyPy & PyPy3 -- see Travis-CI link above.

Rough benchmarks on my machine (mid-2014 Macbook Pro, 2.8GHz i7) using `setup.py
bench` (which times the creation of 1 million cuids):

Version | μs / cuid
--------|----------
CPython 3.6 | 11.368
CPython 3.5 | 9.834
CPython 3.4 | 9.665
CPython 2.7 | 8.869
PyPy 5.6.0 | 0.508

_(Note that timing the creation of fewer IDs changes the way PyPy runs the code, because of JIT warmup --
obviously creating this many IDs takes advantage of the warmed JIT)_

*Note*: For now, this has no dependencies outside the standard library -- in
time this may change, to provide better random numbers and / or performance.
