#include <stdio.h>
#include <stdlib.h>

int size = 0;

typedef struct node {
    int val;
    struct node* next;
} node;

// traverse the list and print elements of linked list
void print_list(node* head) {
    node* current = head;
    while(current != NULL) {
        printf("%d -->", current->val);
        current = current->next;
    }
    printf("\n");
}

// traverse the linked list and count elements
int len(node* head) {
    node* current = head;
    int x = 0;
    while(current != NULL) {
        x++;
        current = current->next;
    }
    return x;
}

// append an element at the end of the linked list
void append(node* head, int val) {
    node* current = head;
    while(current->next != NULL) {
        current = current->next;
    }
    current->next = (node*) malloc(sizeof(node));
    current->next->val = val;
    current->next->next = NULL;
    size++;
}

// remove an element by index
int pop(node* head, int index) {
    int rval = -1;
    node* current = head;
    
    // no elements
    if (size < 1) {
        return rval;
    }

    if (index == -1) {
        // if there is only one element
        if (current->next == NULL) {
            rval = current->val;
            free(current);
            size--;
            return rval;
        }
    
        // get node before tail
        while (current->next->next != NULL) {
            current = current->next;
        }

        rval = current->next->val;
        free(current->next);
        current->next = NULL;
        size--;
    } else {
        node* tmp = NULL;

        for(size_t i = 0; i < index-1; i++) {
           if (current->next == NULL) {
               return rval;
           }
           current = current->next;
        }
        
        if (current->next == NULL) {
            return rval;
        }

        tmp = current->next;
        rval = tmp->val;
        current->next = tmp->next;
        free(tmp);
    }
 
    return rval;
}

// check if ll contains an element
int contain(node* head, int val) {
    int counter = 0;
    while(head != NULL) {
        if (head->val == val) {
            return 1; 
        }
        head = head->next;
        counter++;
    }
    return -1;
}

int main() {
    node* head = NULL;

    head = (node*) malloc(sizeof(node));
    if (head == NULL) {
        return 1;
    }
    
    head->val = 1;
    size++;
    head->next = (node*) malloc(sizeof(node));
    head->next->val = 2;
    head->next->next = NULL;
    size++;
    
    // add an element at the end of the linked list
    printf("Add a new element to ll: 100\n");
    append(head, 100);
    printf("Add a new element to ll: 300\n");
    append(head, 300);

    print_list(head);
    printf("size of the list: %d\n", len(head));
    printf("size of the list from global var size: %d\n", size);

    printf("Linked list contains %d: %d\n", 2, contain(head, 2));
    printf("Linked list does NOT contain %d: %d\n", 200, contain(head, 200));

    // pop last element
    printf("Remove last element\n");
    pop(head, -1);
    print_list(head); 
    printf("Remove element with index 1\n");
    pop(head, 1);
    print_list(head); 

    return EXIT_SUCCESS;
}
