#include "lists.h"

/**
 * insert_node - ...
 * @head: ...
 * @number: ...
 *
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *where = *head;
	listint_t *new = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (where->n > number)
		new->next = where, *head = new;
	else
	{
		while (where->next != NULL && where->next->n <= number)
			where = where->next;
		new->next = where->next;
		where->next = new;
	}
	return (new);
}
