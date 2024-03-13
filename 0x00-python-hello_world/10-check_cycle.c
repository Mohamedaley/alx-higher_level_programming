#include "lists.h"
/**
 * check_cycle - A function to search for cycle in a list
 * @list: the head of the cycle
 * Return: 0 on failure 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (!list)
		return (0);
	fast = list->next;
	slow = list;

	while (fast->next && slow && fast)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
