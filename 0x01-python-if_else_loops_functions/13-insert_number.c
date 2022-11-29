#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node - inserts a number to a sorted linked list
 * @head: the head of the sorted list
 * @number: the number to be added to the linked list
 *
 * Return: the new node (success) null (failure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	
	new_node->n = number;
	printf("%d", new_node->n);
}
