import cffi


def load_sum():
    ffi = cffi.FFI()
    lib = ffi.dlopen("../lib_ctypes/libfibutils.so")

    ffi.cdef("int sum(int* arr, int len);")

    lst = list(range(10, 20))
    len_lst = len(lst)

    arr = ffi.new("int[]", lst)
    print(arr)

    res = lib.sum(arr, len_lst)
    print(f"{res=}, {sum(lst)}")


def load_build():
    builder = cffi.FFI()
    builder.cdef("int mult(int a, int b, int c);")

    builder.set_source(
        "tmp_mult",
        """
        int mult(int a, int b, int c)
        {
            int res = 0;
            res = a * b * c;
            return res;
        }
        """
    )
    builder.compile()


    from tmp_mult import lib

    a, b, c = 2, 5, 9
    res = lib.mult(a, b, c)
    print(f"{res=}, {a * b * c=}")


def run():
    load_sum()
    load_build()


if __name__ == "__main__":
    run()
