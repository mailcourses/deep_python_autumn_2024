from setuptools import setup
from Cython.Build import cythonize


def main():
    setup(
        ext_modules=cythonize(["fibcyth.pyx"]),
    )


if __name__ == "__main__":
    main()
