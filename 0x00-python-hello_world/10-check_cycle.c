#include "lists.h"
/**
 * check_cycle - A function to search for cycle in a list
 * @list: the head of the cycle
 * Return: 0 on failure 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *behind, *forward;

	if (!list || list->next == NULL)
		return (0);

	behind = list->next;
	forward = list->next->next;

	while (behind && forward && forward->next)
	{
		if (behind == forward)
			return (1);

		behind = behind->next;
		forward = forward->next->next;
	}

	return (0);
}
