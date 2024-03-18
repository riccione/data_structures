class Queue:
    def __init__(self):
        self.queue = []

    # add a element to the end of the queue
    # FIFO
    def enque(self, el):
        self.queue.append(el)

    # remove a first element from the queue
    def deque(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        el = self.queue[0]
        self.queue = self.queue[1:]
        return el

    # return a first element from the queue
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

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

    def __repr__(self):
        xs = [str(x) for x in self.queue]
        return ", ".join(xs)

    def __str__(self):
        return self.__repr__()


x = Queue()
print(x.queue)
print(x.is_empty())
for i in range(10):
    x.enque(i)
print(x.queue)
print(x.is_empty())
print(x.contains(9))
print(x.contains(100))
print(x.queue)
x.deque()
x.deque()
print(x.queue)
x.remove(8)
print(x.queue)
x.remove(80)
