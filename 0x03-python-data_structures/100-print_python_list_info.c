#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - print info of Python lists.
* @p: python object
* Return: none
**/
void print_python_list_info(PyObject *p)
{
    int i = 0;
    int size = (int)Py_SIZE(p);
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", list->allocated);

    while (i < size)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
        i++;
    }
}
s
