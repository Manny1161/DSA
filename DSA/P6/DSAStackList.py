#DSAStack code reused from previous pracs
from DSALinkedList import *

class DSAListStack():
    def __init__(self):
        self._stack = DSALinkedList()

    def push(self, val):
        self._stack.insertFirst(val)

    def pop(self):
        return self._stack.removeFirst()

    def top(self):
        return self._stack.peekFirst()

    def isEmpty(self):
        return self._stack.isEmpty()

    def __iter__(self):
        return self._stack.__iter__()

if __name__ == "__main__":
    ls = DSAListStack()
    ls.push(1)
    print(ls.top())
    ls.pop()
    print(ls.top())
