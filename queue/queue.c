/*
 * simple design of queues with arrays in c
 * not safe, just for education purposes
 */
#include <stdio.h>

int arr[100];
int* a;
int size = 0;

typedef struct queue {
    int arr_[100];
    int* p_arr;
    int size_;
} queue;   
 
void enqueue(int val) {
    if (arr) { 
        arr[size] = val;
        a = &arr;
        size++;
    } else {
        printf("Failed to add el to a queue");
    }
}

/* 
 * does not remove an element from the array, just changes pointer
 * not the best solution - need to revisit it
 */
int dequeue() {
    if (arr && size > 0) {
        a = &arr;
        a++;
        size--;
        return arr[0];
    }
    return -1;
}

int peek() {
    if (arr && size > 0) {
        return arr[0];
    }
    return -1;
}

int is_empty() {
    return size;
}

// O(n)
int contains(int val) {
    for (size_t i = 0; i < size; i++) {
        if (arr[i] == val) {
            return 1;
        }
    }
    return 0;
}

// O(n)
int remove_el(int val) {
    return -1;
}

void display() {
    int i = 0;
    while(i < size) {
        printf("%d-", a[i]);
        i++;
    }
    printf("\n");
}

void display_(queue q) {
    for(size_t i = 0; i < q.size_; i++) {
        printf("%d-", q.arr_[i]);
    }
    printf("\n");
}

int main() {
    for(size_t i = 0; i < 10; i++) {
        enqueue(i);
    }
    display();
    dequeue();
    display();

    queue q;
    q.size_ = 0;
    q.arr_[0] = 101;
    q.size_++;
    q.arr_[1] = 102;
    q.size_++;
    display_(q);

    return 0;
}
