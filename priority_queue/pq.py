"""
Priority Queue

Inspired by Willam Fiset Java implementation
https://github.com/williamfiset/Algorithms/
"""

class BinaryHeap():

    heap = []

    def __init__(self, xs):
        heap_size = len(xs)
        for x in xs:
            self.heap.append(x)

        # heapify, O(n)
        i = max(0, heap_size // 2 - 1)
        while i >= 0:
            self.sink(i)
            i -= 1

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.heap.clear()

    def size(self):
        return len(self.heap)

    def peek(self):
        if is_empty:
            return None
        return self.heap[0]
   
    # remote root
    def poll(self):
        return self.remove_at(0)

    # O(n)
    def contains(self, el):
        for x in self.heap:
            if x == el:
                return True
        return False
    
    def display(self):
        n = self.size()
        i = 0
        level = 0
        while i < n:
            level_nodes = 2 ** level
            for j in range(level_nodes):
                if i < n:
                    print(self.heap[i], end=" ")
                    i += 1
                else:
                    break
            print()
            level += 1
        print()
        #for i, x in enumerate(self.heap): 
        #    print(f"{x}--", end="")
        #print()

    # top down node sink O(log(n))
    def sink(self, k):
        #breakpoint()
        heap_size = self.size()
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            # just an assumption that left is the smallest
            smallest = left
                        
            if right < heap_size and self.less(right, left):
                smallest = right

            # stop if cannot sink anymore
            if left >= heap_size or self.less(k, smallest):
                break
            
            self.swap(smallest, k)
            k = smallest

    # bottom up node swim O(log(n))
    def swim(self, k):
        parent = (k - 1) // 2
        while k > 0 and self.less(k, parent):
            self.swap(parent, k)
            k = parent

            parent = (k - 1) // 2

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add(self, el):
        if el is None:
            print("None element cannot be added")
            return

        self.heap.append(el)

        index_of_last_el = self.size() - 1
        self.swim(index_of_last_el)

    # removes a particular element in the heap O(n)
    def remove(self, el) -> bool:
        if el is None:
            return False

        for i, x in self.heap:
            if el == x:
                self.remove_at(i)
                return True
        
        return False

    # removes a node at particular index O(log(n))
    def remove_at(self, i):
        if self.is_empty():
            return None

        index_of_last_el = self.size() - 1
        removed_data = self.heap[i]
        self.swap(i, index_of_last_el)
        
        # removes the last el
        self.heap.pop()

        if i == index_of_last_el:
            return removed_data
        el = self.heap[i]

        self.sink(i)

        # if sinking does not work - try swim
        if self.heap[i] == el:
            self.swim(i)

        return removed_data

    # checks if heap is min
    # k is 0 - root of the heap, needs for recursion
    def is_min_heap(self, k) -> bool:
        heap_size = self.size()
        if k >= heap_size:
            return True

        left = 2 * k + 1
        right = 2 * k + 2

        if left < heap_size and not self.less(k, left):
            return False

        if right < heap_size and not self.less(k, right):
            return False

        # recursion
        return self.is_min_heap(left) and self.is_min_heap(right)


binary_heap = BinaryHeap([0,1,2,3,4,5,6,7])
binary_heap.display()
binary_heap.clear()
binary_heap1 = BinaryHeap([7,6,5,4,3,1])
binary_heap1.display()
binary_heap1.add(10)
binary_heap1.add(2)
binary_heap1.display()
binary_heap1.clear()
binary_heap2 = BinaryHeap([7,6,5,4,3,2,1,0])
binary_heap2.display()
print(binary_heap2.is_min_heap(0))
binary_heap2.poll()
binary_heap2.display()
