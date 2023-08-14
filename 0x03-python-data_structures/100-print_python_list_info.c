#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - print python lists info.
 * @p: pointer to the python object.
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list_p = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
	printf("[*] Allocated = %d\n", list_p->allocated);

	for (i = 0; i < list_p->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, list_p->ob_item[i]->ob_type->tp_name);
}
