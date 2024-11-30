int fib_rec_ctypes(int n)
{
    if (n < 3)
        return 1;

    return fib_rec_ctypes(n - 1) + fib_rec_ctypes(n - 2);
}


int fib_iter_ctypes(int n)
{
    int a = 0;
    int b = 1;

    for (int i = 0; i < n; ++i)
    {
        int tmp = b;
        b = a + b;
        a = tmp;
    }

    return a;
}


int sum(int* arr, int len)
{
    int s = 0;
    for (int i = 0; i < len; ++i)
    {
        s += arr[i];
    }
    return s;
}
