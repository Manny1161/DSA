class DSAListNode:
    def __init__(self, data, prev, next):
        self._data = data
        self._prev = prev
        self._next = next

class DSALinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def _insert(self, val, after):
        if after == None:
            node = DSAListNode(val, self._tail, None)
            self._tail = node
            if self.isEmpty():
                self._head = node
            else:
                node._prev._next = node
        else:
            node = DSAListNode(val, after._prev, after)
            after._prev = node
            if after is self._head:
                self._head = node
            else:
                node._prev._next = node
        
    def _remove(self, val):
        if val is self._head:
            self._head = val._next
        else:
            val._prev._next = val._next

        if val is self._tail:
            self._tail = val._prev
        else:
            val._next._prev = val._prev
        return val._data
        
    def _find(self, val):
        node = self._head
        while node != None and val != node._data:
            node = node._next
        return node

    def __iter__(self):
        def forward_gen(iter):
            while iter != None:
                yield iter._data
                iter = iter._next
        return forward_gen(self._head)

    def isEmpty(self):
        return self._head == None

    def insertFirst(self, val):
        self._insert(val, self._head)

    def insertLast(self, val):
        self._insert(val, None)
    
    def insertBefore(self, val, before):
        self._insert(val, self._find(before))
    
    def peekFirst(self):
        return self._head._data

    def peekLast(self):
        return self._tail._data

    def removeFirst(self):
        return self._remove(self._head)

    def removeLast(self):
        return self._remove(self._tail)

    def remove(self, val):
        return self._remove(self._find(val))

    def find(self, val):
        return self._find(val) != None

    def count(self) -> int:
        return sum(1 for _ in self)

