#include "lists.h"

/**
 * is_palindrome - checks whether a list is palindrome
 * with minimal time complexity and no heap allocations.
 * @head: pointer to the pointer to the head of the list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *middle;
	listint_t *current;
	int size, i;

	slow = fast = *head;
	size = i = 0;

	if (*head == NULL)
		return (1);
	size++;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		size++;
	}
	middle = slow->next;
	fast = slow->next; /* reverse the second half */
	while (middle != NULL && middle->next != NULL)
	{
		current = middle->next;
		middle->next = middle->next->next;
		current->next = fast;
		fast = current;
	}
	slow->next = fast;
	slow = *head;
	for (i = 0; i < size && fast != NULL; i++)
	{ /* compare */
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
