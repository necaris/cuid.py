import sys
import os

from setuptools import setup

VERSION = "0.2"
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as r:
    README = r.read()

setup(
    name='cuid.py',
    version=VERSION,
    description='Fast, scalable unique ID generation',
    long_description=README,
    url='http://github.com/necaris/cuid.py',
    py_modules=['cuid'],
    # license specified by classifier
    author='Rami Chowdhury',
    author_email='rami.chowdhury@gmail.com',
    maintainer='Rami Chowdhury',
    maintainer_email='rami.chowdhury@gmail.com',
    download_url=('http://github.com/necaris/cuid.py/tarball'
                  '/v{}'.format(VERSION)),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
