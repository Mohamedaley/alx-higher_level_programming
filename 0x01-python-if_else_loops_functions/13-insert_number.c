#include "lists.h"
/**
 * insert_node - A function to instert a node in specific place.
 * Developed by Mohamed Ali
 * @head: the head pointer.
 * @number: the data stored.
 * Return: address of new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL, *temp = NULL, *new = NULL;

	ptr = *head, temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->next = NULL, new->n = number;
	if (!(*head))
	{
		*head = new;
		temp = NULL;
		ptr = NULL;
		return (new);
	}
	if (temp->n > number)
	{
		new->next = temp;
		*head = new;
		ptr = NULL;
		return (new);
	}
	ptr = ptr->next;
	if (ptr->n > number)
	{
		temp->next = new, new->next = ptr;
	}
	while (ptr)
	{
		if (ptr->n > number)
		{
			temp->next = new;
			new->next = ptr;
			break;
		}
		ptr = ptr->next;
		temp = temp->next;
	}
	if (ptr == NULL)
		temp->next = new;
	return (new);
}
