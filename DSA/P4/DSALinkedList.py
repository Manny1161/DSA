import pickle as p
import numpy as np
import sys

class DSAListNode:
    def __init__(self, data, prev, next):
        self._data = data
        self._prev = prev
        self._next = next

class DSALinkedList:
    def __init__(self):
        self.DEFAULT_CAPACITY = 100
        self._head = None
        self._tail = None
        self.objects = np.empty(self.DEFAULT_CAPACITY, dtype=object)

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
        #self.interactive(ll)

    def insertLast(self, val):
        self._insert(val, None)
        #self.interactive(ll)
    
    def insertBefore(self, val, before):
        self._insert(val, self._find(before))
    
    def peekFirst(self):
        return self._head._data

    def peekLast(self):
        return self._tail._data

    def _removeFirst(self, ll):
        curr = self._head
        while curr is not None:
            nxt = curr._next
            curr._next = None
            nxt._prev = None
            curr = None
            self._head = nxt
        self.interactive(ll)

    def removeFirst(self, ll):
        return self._removeFirst(ll)

    def _removeLast(self, ll):
        prev = None
        curr = self._head
        while curr._next is not None:
            prev = curr
            curr = curr._next
        if prev:
            prev._next = None
        self.interactive(ll)

    def removeLast(self):
        return self._removeLast(ll)

    def remove(self, val):
        return self._remove(self._find(val))

    def find(self, val):
        return self._find(val) != None

    def write(self, ll):
        p.dump(self, open("tmp.pickle", "wb"))
        self.interactive(ll)

    def read(self, ll):
        '''with open("tmp.pickle", "rb") as f:
            gherkin = p.load(f)
            np.append(self.objects, gherkin)
            print(self.objects)
            f.close()'''
        ll = p.load(open("tmp.pickle", "rb"))
        print(ll)
        
        self.interactive(ll)
        return ll
        
    def print_list(self, ll):
        curr = self._head
        while curr is not None:
            print(curr._data, end=', ')
            curr = curr._next
        self.interactive(ll)

    def menu(self):
        print('''
            [1] Insert First
            [2] Insert Last
            [3] Remove First
            [4] Remove Last
            [5] Display List
            [6] Write Serialised File
            [7] Read Serialised File
            [0] Exit ''')
    
    def interactive(self, ll):
        self.menu()
        choice = int(input('\nSelect your choice...\n'))
        while True:
            if choice == 1:
                val = input('\nEnter a value to add first to the linked list...\n')
                self.insertFirst(val, ll)
            elif choice == 2:
                val = input('\nEnter a value to add to the end of the linked list...\n')
                self.insertLast(val, ll)
            elif choice == 3:
                self.removeFirst(ll)
            elif choice == 4:
                self.removeLast()
            elif choice == 5:
                self.print_list(ll)
            elif choice == 6:
                self.write(ll)
            elif choice == 7:
                ll = self.read(ll)
                
            elif choice == 0:
                sys.exit(0)
            else:
                print('ERROR: INVALID INPUT!')
                self.interactive(ll)

if __name__ == "__main__":
    ll = DSALinkedList()
    '''ll.insertFirst('a')
    ll.insertLast('b')
    iterator = iter(ll)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break'''
    #ll.read(ll)
    
    #print(ll.isEmpty())
    #ll.insertFirst("a")
    #print(ll.peekFirst())
    #ll.insertLast("b")
    #print(ll.peekLast())
    ll.interactive(ll)

