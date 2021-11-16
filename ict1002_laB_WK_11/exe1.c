#include <stdio.h>
#include <string.h>

struct grade_node { 
char surname[20]; 
double grade; 
struct grade_node *next; 
}; 
typedef struct grade_node GRADE_NODE; 
typedef GRADE_NODE *GRADE_NODE_PTR;


void printList(GRADE_NODE_PTR n)
{
    while (n != NULL) {
        printf(" %s ", n->surname);
        printf(" %f\n", n->grade);
        n = n->next;
    }
}

int main() {
    GRADE_NODE_PTR head = NULL;
    GRADE_NODE node1 = {"Adams", 85.0, NULL};
    GRADE_NODE node2 = {"Pritchard", 66.5, NULL};
    GRADE_NODE node3 = {"Jones", 91.5, NULL};


    head = &node1;
    node1.next = &node3;
    node3.next = &node2;

    printList(head);


    return 0;
}