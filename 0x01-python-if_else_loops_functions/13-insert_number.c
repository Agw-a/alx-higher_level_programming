#include "lists.h"

/**
 * insert_node-inserts a number into a sorted singly linked list.
 * @head:address of the head of the list
 * @number:number to beadded to list
 * Return:address of new node
 * Description:a function in C that inserts a number into a
 * sorted singly linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *previousnode, *tempnode;

	if (!head)
	return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
	return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (!*head)
	{
		*head = newnode;
		return (newnode);
	}
	tempnode = *head;
	if ((*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (tempnode && (tempnode->n < number))
	{
		previousnode = tempnode;
		tempnode = tempnode->next;
	}
	newnode->next = tempnode;
	previousnode->next = newnode;
	return (newnode);
}
