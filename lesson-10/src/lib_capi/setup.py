from setuptools import setup, Extension


def main():
    setup(
        name="fibutils",
        version="1.0.1",
        ext_modules=[Extension("fibutils", ["fibutils.c"])],
    )


if __name__ == "__main__":
    main()
