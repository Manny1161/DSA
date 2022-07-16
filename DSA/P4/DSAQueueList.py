#DSAQueue code reused from previous pracs

from DSALinkedList import *

class DSAListQueue():
    def __init__(self):
        self._queue = DSALinkedList()

    def enqueue(self, val):
        self._queue.insertLast(val)

    def dequeue(self):
        return self._queue.removeFirst()

    def peek(self):
        return self._queue.peekFirst()

    def isEmpty(self):
        return self._queue.isEmpty()

    def __iter__(self):
        return self._queue.__iter__()

if __name__ == "__main__":
    lq = DSAListQueue()
    lq.enqueue(1)
    print(lq.peek())
    lq.dequeue()
    print(lq.peek())



