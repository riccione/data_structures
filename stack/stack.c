#include <stdio.h>
#include <stdlib.h>

int size = 0;

typedef struct node {
    int val;
    struct node* next;
} node;

node* head = NULL;

// add node to the head
void push(int val);

// remove node from the head
int pop();

void print_ll(node* head);

int main() {
    for(size_t i = 100; i < 110; i++) {
        push(i);
    }
    print_ll(head);

    pop();

    print_ll(head);

    return 0;
}

void print_ll(node* head) {
    node* current = head;
    while(current != NULL) {
        printf("%d-->", current->val);
        current = current->next;
    }
    printf("NULL\n");
}

void push(int val) {
    node* t = (node*) malloc(sizeof(node));
    t->val = val;
    size++;

    if (head == NULL) {
        head = t;
        head->next = NULL;
    } else {
        t->next = head;
        head = t;
    }
}

int pop() {
    int val = -1;
    if (head == NULL) {
        return val;
    }
    
    node* next_node = head->next;
    val = head->val;
    free(head);
    head = next_node;
    size--;
    return val;
}
