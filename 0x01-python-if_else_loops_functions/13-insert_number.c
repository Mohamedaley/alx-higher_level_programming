#include "lists.h"
/**
 * insert_node - A function to instert a node in specific place
 * @head: the head pointer
 * @number: the data stored
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL, *temp = NULL;
	listint_t *new = NULL;

	if (!(*head))
		return (NULL);

	ptr = *head;
	temp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	while (ptr)
	{
		if (number == 0)
		{
			new->next = (*head);
			(*head) = new;
		}
		else if (number < ptr->n)
		{
			while (temp != NULL && temp != ptr)
			{
				if (temp->next != ptr)
					temp = temp->next;
			}
			temp->next = new;
			new->next = ptr;
		}
		ptr = ptr->next;
	}
	return (new);
}
