class Queue:
    def __init__(self):
        self.queue = []
    
    # add a element to the end of the queue
    # FIFO
    def enqueue(self, el):
        self.queue.append(el)

    # remove a first element from the queue
    def dequeue(self):
        el = self.queue[0]
        self.queue = self.queue[1:]
        return el

    # return a first element from the queue
    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return bool(len(self.queue))

    def contains(self, el):
        return el in self.queue

    # O(n)
    def remove(self, el):
        if self.contains(el) or not self.is_empty():
            r = []
            for e in self.queue:
                if e != el:
                    r.append(e)
            self.queue = r
        else:
            print(f"No element {el} in the queue")

x = Queue()
print(x.queue)
print(x.is_empty())
for i in range(10):
    x.enqueue(i)
print(x.queue)
print(x.is_empty())
print(x.contains(9))
print(x.contains(100))
print(x.queue)
x.dequeue()
x.dequeue()
print(x.queue)
x.remove(8)
print(x.queue)
x.remove(80)
