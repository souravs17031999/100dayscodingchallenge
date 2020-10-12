// constructing linked list node structure using structs in C
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

int main(void)
{
    struct Node *head = NULL;
    struct Node *second = NULL;
    struct Node *third = NULL;
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    printf("value stored in head next: %d\n", head->next);
    printf("addres of second %d\n", &second);
    printf("value stored in second next: %d\n", second->next);
    printf("addres of third %d\n", &third);
    printf("value stored in third next: %d", third->next);

    return 0;
}