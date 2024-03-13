#include "lists.h"
/**
 * check_cycle - A function to search for cycle in a list
 * @list: the head of the cycle
 * Return: 0 on failure 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (list == NULL)
		return (0);
	fast = list;
	slow = list;

	while (fast->next->next)
	{
		if (fast == slow)
		{
			fast = NULL;
			slow = NULL;
			return (1);
		}
		slow = slow->next;
		fast = fast->next;
	}
	fast = NULL;
	slow = NULL;
	return (0);
}
