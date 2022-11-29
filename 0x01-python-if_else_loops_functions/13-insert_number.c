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
    listint_t *current = *head;
    listint_t *previous = NULL;
	
	new_node->n = number;
	while (current != NULL)
    {
        if (*head->n > new_node->n)
        {
            new_node->next = current;
            if (previous != NULL)
                previous->next = new_node;
            return (new_node);
        }
        previous = current;
        current = current->next;
    }
    return (NULL);
}
