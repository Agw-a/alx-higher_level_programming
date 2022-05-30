#include "lists.h"

/**
 * @brief 
 * 
 */
int check_cycle(listint_t *list)
{
    listint_t *fast, *slow;
    slow = list;
    fast = list;

    if(!list || !list->next)
    return (0);

    for (;fast && fast->next;)
    {
        fast = fast->next->next;
        slow = slow->next;
        if (fast == slow)
        {
            return (1);
        }
    }
    return (0);
}