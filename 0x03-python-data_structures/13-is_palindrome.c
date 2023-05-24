#include "lists.h"

/**
 * list_length - Finds the number of elements in a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Number of elements in the linked list.
 */
size_t list_length(listint_t *head)
{
	size_t count = 0;

	if (head == NULL)
		return (0);

	for (; head != NULL; head = head->next)
		count++;

	return (count);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome. Otherwise, 0.
 */
int is_palindrome(listint_t **head)
{
	int *arr, i = 0, j = 0, length = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);

	temp = *head;
	length = list_length(temp);
	arr = (int *)malloc(sizeof(int) * length);
	if (arr == NULL)
		return (2);

	temp = *head;
	while (temp != NULL)
	{
		arr[j] = temp->n;
		j++;
		temp = temp->next;
	}

	for (i = 0, j = length - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}

	return (1);
}
