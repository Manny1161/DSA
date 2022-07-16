import numpy as np
from abc import ABC, abstractmethod

class DSAQueue(ABC):

    @abstractmethod
    def enqueue(item : object):
        pass

    @abstractmethod
    def dequeue() -> object:
        pass

    @abstractmethod
    def peek() -> object:
        pass

    @abstractmethod
    def isEmpty() -> bool:
        pass

    @abstractmethod
    def isFull() -> bool:
        pass

    @abstractmethod
    def count() -> bool:
        pass


class DSAShufflingQueue(DSAQueue):
    def __init__(self):
        self.DEFAULT_CAPACITY = 100
        self._queue = np.empty(self.DEFAULT_CAPACITY, dtype=object)
        self._count = 0

    def enqueue(self, item : object):
        self._queue[self._count] = item
        self._count += 1

    def dequeue(self) -> object:
        item = self._queue[0]
        self._count -= 1
        for i in range(self._count):
            self._queue[i] = self._queue[i + 1]
        return item

    def peek(self) -> object:
        return self._queue[0]

    def isEmpty(self) -> object:
        return self._count == 0

    def isFull(self) -> object:
        return self._count == len(self._queue)

    def count(self) -> object:
        return self._count


class DSACircularQueue(DSAQueue):

    def __init__(self):
        self.DEFAULT_CAPACITY = 100
        self._queue = np.empty(self.DEFAULT_CAPACITY, dtype=object)
        self._count = 0
        self._head = 0

    def enqueue(self, item : object):
        self._queue[(self._head + self._count) % len(self._queue)] = item
        self._count += 1

    def dequeue(self) -> object:
        self._count -= 1
        self._head = (self._head + 1) % len(self._queue)
        return self._queue[self._head - 1]

    def peek(self) -> object:
        return self._queue[self._head]

    def isEmpty(self) -> object:
        return self._count == 0

    def isFull(self) -> object:
        return self._count == len(self._queue)

    def count(self) -> int:
        return self._count

if __name__ == "__main__":
    CQ = DSACircularQueue()
    print(CQ.isEmpty())
    CQ.enqueue(1)
    CQ.enqueue(2)
    CQ.enqueue(3)
    CQ.enqueue(4)
    CQ.enqueue(5)
    CQ.enqueue(6)
    CQ.enqueue(7)
    print(CQ.peek())
    CQ.dequeue()
    print(CQ.peek())
    print(CQ.count())
    SQ = DSAShufflingQueue()
    print(SQ.isEmpty())
    SQ.enqueue(1)
    SQ.enqueue(2)
    SQ.enqueue(3)
    SQ.enqueue(4)
    SQ.enqueue(5)
    print(SQ.peek())
    SQ.dequeue()
    print(SQ.peek())
    print(SQ.count())

  

