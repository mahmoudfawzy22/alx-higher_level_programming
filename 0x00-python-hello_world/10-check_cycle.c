#include<stdio.h>
#include<stdlib.h>

#include <stdlib.h>

int check_cycle(listint_t *list)
{
	listinit_t *slow = list, *fast = list;

	while (fast && fast->)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return(1);
	
	}
	return(0);
}
