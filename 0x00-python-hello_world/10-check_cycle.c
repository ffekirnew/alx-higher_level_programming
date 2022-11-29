#include "lists.h"
#include <stdio.h>


/**
 * check_cycle - will check if there is a cycle in a linked hare
 * @list: the linked list to be checked
 *
 * Return: 0 if there's no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
    listint_t *turtle = list->next;
    listint_t *hare;


    if (list->next == NULL)
        return (0);

    hare = list->next->next;
    while ((turtle->next != NULL) && (hare->next->next != NULL))
    {
        if (turtle->n == hare->n)
            return (1); 
        turtle = turtle->next;
        hare = hare->next->next;
    }
    return (0);
}
