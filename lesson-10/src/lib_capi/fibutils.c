#include <stdlib.h>
#include <stdio.h>

#include <Python.h>


int fib_rec_capi_impl(int n)
{
    if (n < 3)
        return 1;

    return fib_rec_capi_impl(n - 1) + fib_rec_capi_impl(n - 2);
}


PyObject* fibutils_fib_rec_capi(PyObject* self, PyObject* args)
{
    int n = 0;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("WRONG arg");
        return NULL;
    }

    int res = fib_rec_capi_impl(n);
    return PyLong_FromLong(res);
    /* return Py_BuildValue(res); */
}


PyObject* fibutils_fib_iter_capi(PyObject* self, PyObject* args)
{
    int n = 0;
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        printf("WRONG arg");
        return NULL;
    }

    int a = 0;
    int b = 1;

    for (int i = 0; i < n; ++i)
    {
        int tmp = b;
        b = a + b;
        a = tmp;
    }
    return PyLong_FromLong(a);
}


static PyMethodDef methods[] = {
    {"fib_rec_capi", fibutils_fib_rec_capi, METH_VARARGS, "c-api fib rec"},
    {"fib_iter_capi", fibutils_fib_iter_capi, METH_VARARGS, "c-api fib iter"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef module_fibutils = {
    PyModuleDef_HEAD_INIT, "fibutils", NULL, -1, methods
};


PyMODINIT_FUNC PyInit_fibutils()
{
    return PyModule_Create( &module_fibutils );
}
