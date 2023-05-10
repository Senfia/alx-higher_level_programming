#ifndef _LISTS_H
#define _LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @num: int
 * @next: pointer to the next node
 */
typedef struct listint_s
{
	int num;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *head);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int num);

#endif
