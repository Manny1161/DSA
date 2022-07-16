import unittest
import numpy as np
import itertools

class DSAHeapEntry:
    def __init__(self, priority, value):
        self._priority = priority
        self._value = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, p):
        self._priority = p

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, p):
        self._value = p

    def __str__(self):
        return str(self._priority) + ' ' + str(self._value)

class DSAHeap:    
    def __init__(self, size):
        self._heapArr = np.zeros(size, dtype=object)
        for i in range(len(self._heapArr)):
            self._heapArr[i] = DSAHeapEntry(None, None)
        self._count = 0

    def _add(self, priority, value):
        if len(self) == len(self._heapArr):
            raise ValueError('Heap is full!')
        self._heapArr[len(self)].priority = priority
        self._heapArr[len(self)].value = value
        self.trickleUp(len(self))
        self._count += 1

    def add(self, priority, value):
        return self._add(priority, value)

    def __len__(self):
        return self._count

    def _remove(self):
        if len(self) == 0:
            raise ValueError('Heap is empty!')
        value = self._heapArr[0].value
        self._count -= 1
        self._heapArr[0], self._heapArr[len(self)] = self._heapArr[len(self)], self._heapArr[0]
        self.trickleDown(0)
        return value
        
    def remove(self):
        return self._remove()

    def _heapify(self):
        for i in reversed(range(int(len(self)/2)-1)):
            self.trickleDown(i)
    
    def heapify(self):
        return self._heapify()

    def _heapSort(self):
        self.heapify()
        for i in reversed(range(1, len(self))):
            self._heapArr[0], self._heapArr[i] = self._heapArr[i], self._heapArr[0]
            self._count -= 1
            self.trickleDown(0)
    
    @staticmethod
    def heapSort(values):
        heap = DSAHeap(len(values))
        for i in range(len(values)):
            heap._heapArr[i].priority = values[i][0]
            heap._heapArr[i].value = values[i][1]
        heap._count = len(values)
        heap._heapSort()

    def read(self):
        with open("RandomNames7000(2).csv", "r") as f:
            for l in f:
                student = l.rstrip("\n").split(",")
                for l1, l2 in zip(sorted(student), DSAHeap.heapSort(student)):
                    self.assertEqual(x1[0], x2[0])


    def _trickleUp(self, index):
        parent = int((index-1)/2)
        if index > 0 and self._heapArr[parent].priority < self._heapArr[index].priority:
            self._heapArr[parent], self._heapArr[index] = self._heapArr[index], self._heapArr[parent]
            self._trickleUp(parent)

    def trickleUp(self, index):
        return self._trickleUp(index)

    def _trickleDown(self, index):
        left = index*2+1
        right = left +1
        temp = 0
        if left < len(self):
            temp = left
        if right < len(self) and self._heapArr[right].priority > self._heapArr[left].priority:
            temp = right
        if temp != 0 and self._heapArr[temp].priority > self._heapArr[index].priority:
            self._heapArr[temp], self._heapArr[index] = self._heapArr[index], self._heapArr[temp]
            self._trickleDown(temp)
    
    def trickleDown(self, index):
        return self._trickleDown(index)

    def print(self):
        for i in range(self._count):
            print(self._heapArr[i])    




if __name__ == "__main__":
    h = DSAHeap(10)
    h.add(10, 'ff')
    h.add(11, 'fff')
    h.add(13, 'i')
    h.add(14, 'k')
    h.add(15, 'id')
    h.add(1, 'ok')
    h.remove()
    h.print()
