#include <stdio.h>
#include <stdlib.h>
#include "Python.h"

/**
 * print_python_list_info - print python lists info.
 * @p: pointer to the python object.
 */
void print_python_list_info(PyObject *p)
{
	int i, size;
	PyListObject *list_p = (PyListObject *)p;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", list_p->allocated);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, list_p->ob_item[i]->ob_type->tp_name);
}
