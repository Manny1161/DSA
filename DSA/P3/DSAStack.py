import numpy as np;

class DSAStack:

    def __init__(self):
        self.DEFAULT_CAPACITY = 100
        self.stack = np.empty(1, dtype=object)
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        return len(self.stack) == 1

    def isFull(self):
        return len(self.stack) == self.DEFAULT_CAPACITY

    def push(self, val):
        if not self.isFull():
            self.stack = np.append(self.stack, val)
            self.count += 1
        else:
            print('stack is full')
    
    def pop(self):
        if not self.isEmpty():
            topVal = self.stack[-1]
            self.count -= 1 
            self.stack = np.delete(self.stack , 0)
            return topVal
        else:
            print('stack is empty')

    def top(self):
            return self.stack[len(self.stack)-1]

    def getStack(self):
        return self.stack

    def __repr__(self):
        return self.stack

if __name__ == "__main__":
    s = DSAStack()
    print(s.isEmpty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.isEmpty())
    print(s.top())
    print(s.getCount())
    s.pop()
    s.pop()
    s.pop()
    print(s.isEmpty())

