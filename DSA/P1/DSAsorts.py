import numpy as np

#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A) -1 -i):
            if A[j]>A[j+1]: #  check if left is bigger than right value
                A[j] = A[j+1] #  swap left w/ right value
                A[j+1] = A[j] #  swap right w/ left value
    return A 

arr = np.empty(0)
with open('RandomNames7000(2).csv', 'r') as f:
    for line in f.readlines():
        bublist = line.split(',')[0]
        arr = np.append(arr, bublist)
result = bubbleSort(arr)

with open('bubblesorted.csv', 'w') as f:
    f.write(str(result))
    f.close
    
def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i] #  use this var as the lowest variable to test against
        j = i-1 #  use this var as the left value in the array
        while j>=0 and key < A[j]: #  checks if the left is bigger than right value
            A[j+1] = A[j] #  swap right w/ left value if its lower
            j -= 1
        A[j+1] = key #  assign the right value as the key to restart the sort
    return A
arr = np.empty(0)
with open('RandomNames7000(2).csv', 'r') as f:
    for line in f.readlines():
        insertlist = line.split(',')[0]
        arr = np.append(arr, insertlist)
result = insertionSort(arr)

with open('insertsorted.csv', 'w') as f:
    f.write(str(result))
    f.close()

def selectionSort(A):
    for i in range(0, len(A)-1): #  outer loop
        minVal = i
        for j in range(i+1, len(A)): #  inner loop
            if A[j]<A[minVal]:
                minVal = j #  swap value if right is lower than left (minVal)
        temp = A[minVal]
        A[minVal] = A[i]
        A[i] = temp
    #if minVal != i:
    #    A[i] = A[minVal] # swap current value w/ minVal
    #    A[minVal] = A[i]
    return A

arr = np.empty(0)
with open('RandomNames7000(2).csv', 'r') as f:
    for line in f.readlines():
        selectlist = line.split(',')[0]
        arr = np.append(arr, selectlist)
result = selectionSort(arr)

with open('selectsorted.csv', 'w') as f:
    f.write(str(result))
    f.close()


def mergeSort(A, leftidx, rightidx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2

        mergeSort(arr, leftIdx, midIdx)
        mergeSort(arr, midIdx+1, rightIdx)

        merge(arr, leftIdx, midIdx, rightIdx)

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ii = midIdx - leftIdx + 1
    jj = rightIdx - midIdx

    L = [0] * ii
    R = [0] * jj

    for i in range(0, ii):
        L[i] = arr[leftIdx + i]

    for j in range(0, jj):
        R[j] = arr[midIdx + 1 + j]

    i = 0
    j = 0
    k = leftIdx

    while i < ii and j < jj:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1
    while i < ii:
        arr[k] = L[i]
        i = i + 1
        k = k + 1


def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


