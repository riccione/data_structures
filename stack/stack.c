#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int size = 0;

typedef struct node {
    int val;
    struct node* next;
} node;

node* head = NULL;

bool is_empty();

// add node to the head
void push(int val);

// remove node from the head
int pop();

void print_ll(node* head);

int len();

int peek();

int main() {
    for(size_t i = 100; i < 110; i++) {
        push(i);
    }
    printf("is empty %s\n", is_empty()?"true":"false");
    print_ll(head);

    printf("pop %d\n", pop());
    printf("Size: %d\n", len());
    printf("pop %d\n", pop());

    print_ll(head);

    return 0;
}

bool is_empty() {
    return size == 0;
}

int len() {
    return size;
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
        printf("Err: pop from an empty stack\n");
        return EXIT_FAILURE;
    }
    
    node* next_node = head->next;
    val = head->val;
    free(head);
    head = next_node;
    size--;
    return val;
}

int peek() {
    if (head == NULL) {
        printf("Err: peek from an empty stack\n");
        return EXIT_FAILURE;
    }
    return head->val;
}
