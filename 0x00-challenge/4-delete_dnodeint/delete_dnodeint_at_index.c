#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head, *tmp;
	unsigned int p = 0;

	if (*head == NULL)
		return (-1);
	saved_head = *head;
	while (p++ < index && *head != NULL)
		*head = (*head)->next;
	if (p != index)
	{
		*head = saved_head;
		return (-1);
	}
	if (index == 0)
	{
		tmp = (*head)->next;
		free(*head);
		*head = tmp;
		if (tmp != NULL)
			tmp->prev = NULL;
	}
	else
	{
		(*head)->prev->prev = (*head)->prev;
		if ((*head)->next)
		{
			(*head)->prev->next = (*head)->next;
			(*head)->next->prev = (*head)->prev;
		}
		free(*head);
		*head = saved_head;
	}
	return (1);
}
