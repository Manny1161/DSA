from enum import Enum
import numpy as np

class DSAHashEntry:
    class status(Enum):
        EMPTY = -1
        USED = 0
        FULL = 1

    def __init__(self):
        self._key = None
        self._value = None
        self._state = DSAHashEntry.status.EMPTY
    
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
    


class DSAHashTable:
    def __init__(self):
        self.size = 100
        self._hashArray = np.empty(DSAHashTable._nextPrime(self.size), dtype=object)
        for i in range(len(self._hashArray)):
            self._hashArray[i] = DSAHashEntry()
        self._count = 0
        self.minLoadFactor = 0
        self.maxLoadFactor = 0.5
        self.resizeFactor = 2
        self._autoResize = True
        self._minLoadFactor = self.minLoadFactor
        self._maxLoadFactor = self.maxLoadFactor
        self._resizeFactor = self.resizeFactor
        

    def put(self, key, value):
        candidate = self._find(key)
        if candidate is None or candidate.state != DSAHashEntry.status.FULL:
            # Inserting into table
            self._count += 1
            if self._autoResize:
                if self._resizeIfNeeded():
                    candidate = self._find(key)
            candidate.state = DSAHashEntry.status.FULL
            candidate.key = key
        candidate.value = value

    def get(self, key):
        candidate = self._find(key)
        if candidate is None or candidate.state != DSAHashEntry.status.FULL:
            raise ValueError("Key not found.")
        return candidate.value

    def hasKey(self, key):
        candidate = self._find(key)
        return candidate is not None and candidate.state == DSAHashEntry.status.FULL

    def remove(self, key):
        candidate = self._find(key)
        if candidate is None or candidate.state != DSAHashEntry.status.FULL:
            raise ValueError("Key not found.")
        self._count -= 1
        if self._autoResize:
            if self._resizeIfNeeded():
                candidate = self._find(key)
        candidate.state = DSAHashEntry.status.USED
        candidate.key = None
        value = candidate.value
        candidate.value = None
        return value

    def loadFactor(self):
        return len(self) / len(self._hashArray)

    def __len__(self):
        return self._count

    # Return None if there is no available space for the key
    def _find(self, key):
        i = DSAHashTable._hash(key, len(self._hashArray))
        stepHash = DSAHashTable._stepHash(key, len(self._hashArray))
        candidate = self._hashArray[i]
        jumps = 0
        while candidate.key != key and candidate.state != DSAHashEntry.status.EMPTY and jumps < len(self._hashArray):
            jumps += 1
            i = (i + stepHash) % len(self._hashArray)
            candidate = self._hashArray[i]

        if jumps == len(self._hashArray):
            candidate = None
        return candidate

    def _resizeIfNeeded(self):
        resized = False
        if self.loadFactor() > self._maxLoadFactor:
            self._resize(ceil(len(self._hashArray) * self._resizeFactor))
            resized = True
        elif self.loadFactor() < self._minLoadFactor:
            # Make consecutive remove as fast as possible
            self._resize(ceil(len(self) / self._maxLoadFactor))
            resized = True
        return resized

    def _resize(self, size):
        newTable = DSAHashTable(size, _autoResize=False)
        for k, v in self:
            newTable.put(k, v)
        self._hashArray = newTable._hashArray

    def __iter__(self):
        def hashIter(hashArray):
            for x in hashArray:
                if x.state == DSAHashEntry.status.FULL:
                    yield (x.key, x.value)
        return hashIter(self._hashArray)

    def _hash(key, len):
        return DSAHashTable._javaStrHash(key) % len

    def _stepHash(key, len):
        return DSAHashTable._fnvHash(key) % (len - 1) + 1

    def _packKey(key):
        import struct
        if isinstance(key, int):
            key = struct.pack("i", key)
        elif isinstance(key, str):
            key = key.encode()
        else:
            raise ValueError("Unsupported key type. Use str or int instead.")
        return key


    # Hash function requirements:
    # Fit within the size of the array
    # Fast to compute
    # Repeatable
    # Distribute evenly

    def _javaStrHash(key):
        hash = 0
        for x in DSAHashTable._packKey(key):
            hash = 31 * hash + x
        return hash


    def _fnvHash(key):
        hash = 2166136261
        for x in DSAHashTable._packKey(key):
            # Force overflow
            hash = ((hash * 16777619) % 2**64) ^ x
        return hash

    def _nextPrime(x):
        if x < 3:
            x = 2
        else:
            # Can be made more efficient
            x = x - 1 if x % 2 == 0 else x - 2
            isPrime = False
            while not isPrime:
                i = 3
                x += 2
                isPrime = True
                while i ** 2 <= x and isPrime:
                    if x % i == 0:
                        isPrime = False
                    i += 2
        return x

if __name__ == "__main__":
    table = DSAHashTable()
    table.put('1', 'one')
    table.put('2', 'two')
    table.put('3', 'three')
    print(table.get('1'))
    print(table.get('3'))
    table.remove('1')
    table.__iter__.hashIter(table)

    
    
