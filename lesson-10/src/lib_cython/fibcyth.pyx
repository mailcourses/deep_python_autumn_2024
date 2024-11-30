cpdef fib_rec_cy(int n):
    if n < 3:
        return 1

    return fib_rec_cy(n - 1) + fib_rec_cy(n - 2)


cpdef fib_iter_cy(int n):
    cdef int a = 0
    cdef int b = 1

    for _ in range(n):
        a, b = b, a + b

    return a
