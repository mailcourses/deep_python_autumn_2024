import ctypes


def load_sum():
    lib = ctypes.cdll.LoadLibrary("./libfibutils.so")
    lib.sum.argstype = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    lib.sum.restype = ctypes.c_int

    lst = list(range(10, 20))
    len_lst = len(lst)

    arr_int_type = ctypes.c_int * len_lst
    res = lib.sum(arr_int_type(*lst), len_lst)

    print(f"{res=}, {sum(lst)}")


def load_std():
    lib = ctypes.CDLL(None)
    lib.strstr.argstype = [ctypes.c_char_p, ctypes.c_char_p]
    lib.strstr.restype = ctypes.c_char_p

    print(f'{lib.strstr(b"ababc", b"ba")=}')
    print(f'{lib.strstr(b"ababc", b"qwerrt")=}')
    print(f'{lib.strstr(b"ababc", b"bc")=}')


def run():
    load_sum()
    load_std()


if __name__ == "__main__":
    run()
