#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle in it
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, else, 0
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	listint_t *slower = list;
	listint_t *faster = list->next;

	for (; faster && faster->next; slower = slower->next,
	faster = faster->next->next)
	{
		if (faster == slower || faster->next == slower)
		return (1);
	}

	return (0);
}

