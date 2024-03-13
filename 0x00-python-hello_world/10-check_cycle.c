#include "lists.h"
/**
 * check_cycle - A function to search for cycle in a list
 * @list: the head of the cycle
 * Return: 0 on failure 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	while (slow)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
