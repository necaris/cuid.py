import os

from setuptools import setup, Command


VERSION = "0.2"
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as r:
    README = r.read()


class bench(Command):
    description = "run lightweight benchmarks"
    user_options = []  # distutils complains if this is not here.

    def __init__(self, *args):
        self.args = args[0]  # so we can pass it to other classes
        Command.__init__(self, *args)

    def initialize_options(self):  # distutils wants this
        pass

    def finalize_options(self):    # this too
        pass

    def run(self):
        """Ensure that several cuids can be generated per millisecond"""
        import timeit
        setup_stmt = "import cuid; g = cuid.CuidGenerator()"
        timed_stmt = "g.cuid()"
        times = 999999
        time_to_run = timeit.timeit(timed_stmt, setup=setup_stmt, number=times)
        time_each = time_to_run / times
        print("%d cuids in %f s (%f us per cuid, %f per sec)" %
              (times, time_to_run, time_each * 1000000, 1.0 / time_each))


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
    cmdclass={"bench": bench},
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
