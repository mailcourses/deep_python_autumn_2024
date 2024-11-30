import ctypes
import time

import cffi
import fibutils
import fibcyth


def fib_rec_py(n: int) -> int:
    if n < 3:
        return 1

    return fib_rec_py(n - 1) + fib_rec_py(n - 2)


def fib_iter_py(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def time_native_python(n_rec, n_iter):
    start = time.time()
    res = fib_rec_py(n_rec)
    end = time.time()
    print(f"[python] rec fib({n_rec}) = {res}, time = {end - start}")

    start = time.time()
    res = fib_iter_py(n_iter)
    end = time.time()
    print(f"[python] iter fib({n_iter}) = {res}, time = {end - start}")


def time_ctypes(n_rec, n_iter):
    lib = ctypes.cdll.LoadLibrary("./lib_ctypes/libfibutils.so")

    lib.fib_rec_ctypes.argstype = [ctypes.c_int]
    lib.fib_rec_ctypes.restype = ctypes.c_int

    lib.fib_iter_ctypes.argstype = [ctypes.c_int]
    lib.fib_iter_ctypes.restype = ctypes.c_int

    start = time.time()
    res = lib.fib_rec_ctypes(n_rec)
    end = time.time()
    print(f"[ctypes] rec fib({n_rec}) = {res}, time = {end - start}")

    start = time.time()
    res = lib.fib_iter_ctypes(n_iter)
    end = time.time()
    print(f"[ctypes] iter fib({n_iter}) = {res}, time = {end - start}")


def time_cffi(n_rec, n_iter):
    ffi = cffi.FFI()
    lib = ffi.dlopen("./lib_ctypes/libfibutils.so")

    ffi.cdef(
        "int fib_rec_ctypes(int n);\n"
        "int fib_iter_ctypes(int n);\n"
    )

    start = time.time()
    res = lib.fib_rec_ctypes(n_rec)
    end = time.time()
    print(f"[cffi] rec fib({n_rec}) = {res}, time = {end - start}")

    start = time.time()
    res = lib.fib_iter_ctypes(n_iter)
    end = time.time()
    print(f"[cffi] iter fib({n_iter}) = {res}, time = {end - start}")


def time_c_api(n_rec, n_iter):
    start = time.time()
    res = fibutils.fib_rec_capi(n_rec)
    end = time.time()
    print(f"[c-api] rec fib({n_rec}) = {res}, time = {end - start}")

    start = time.time()
    res = fibutils.fib_iter_capi(n_iter)
    end = time.time()
    print(f"[c-api] iter fib({n_iter}) = {res}, time = {end - start}")


def time_cython(n_rec, n_iter):
    start = time.time()
    res = fibcyth.fib_rec_cy(n_rec)
    end = time.time()
    print(f"[cython] rec fib({n_rec}) = {res}, time = {end - start}")

    start = time.time()
    res = fibcyth.fib_iter_cy(n_iter)
    end = time.time()
    print(f"[cython] iter fib({n_iter}) = {res}, time = {end - start}")


def run():
    n_rec, n_iter = 37, 45

    time_native_python(n_rec, n_iter)
    print("-----------\n")

    time_ctypes(n_rec, n_iter)
    print("-----------\n")

    time_cffi(n_rec, n_iter)
    print("-----------\n")

    time_c_api(n_rec, n_iter)
    print("-----------\n")

    time_cython(n_rec, n_iter)


if __name__ == "__main__":
    run()
