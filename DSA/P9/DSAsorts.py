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

    
def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i] #  use this var as the lowest variable to test against
        j = i-1 #  use this var as the left value in the array
        while j>=0 and key < A[j]: #  checks if the left is bigger than right value
            A[j+1] = A[j] #  swap right w/ left value if its lower
            j -= 1
        A[j+1] = key #  assign the right value as the key to restart the sort
    return A


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



def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    mergeSortRecurse(A, 0, len(A) - 1)


def mergeSortRecurse(A, left, right):
    if left < right:
        mid = int((left + right) / 2)
        mergeSortRecurse(A, left, mid)
        mergeSortRecurse(A, mid + 1, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    temp = np.zeros(right - left + 1)
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1
    for x in A[i:mid + 1]:
        temp[k] = x
        k += 1
    for x in A[j:right + 1]:
        temp[k] = x
        k += 1
    for i, x in enumerate(temp):
        A[i + left] = x

def quickSort(A, *, pivotFunc, threeWay=False):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    if threeWay:
        quickSort3wayRecurse(A, 0, len(A) - 1, pivotFunc)
    else:
        quickSortRecurse(A, 0, len(A) - 1, pivotFunc)


def quickSortRecurse(A, left, right, pivotFunc):
    if right > left:
        mid = (left + right) / 2
        pivot = pivotFunc(A, left, right)
        pivot = doPartitioning(A, left, right, pivot)
        quickSortRecurse(A, left, pivot - 1, pivotFunc)
        quickSortRecurse(A, pivot + 1, right, pivotFunc)

def quickSort3wayRecurse(A, left, right, pivotFunc):
    if right > left:
        pivot = pivotFunc(A, left, right)
        i, j = doPartitioning3way(A, left, right, pivot)
        quickSort3wayRecurse(A, left, i - 1, pivotFunc)
        quickSort3wayRecurse(A, j + 1, right, pivotFunc)

def doPartitioning3way(A, left, right, pivot):
    i = left
    j = right
    k = left
    pivotVal = A[pivot]
    while k <= j:
        if A[k] < pivotVal:
            A[k], A[i] = A[i], A[k]
            i += 1
            k += 1
        elif A[k] > pivotVal:
            A[k], A[j] = A[j], A[k]
            j -= 1
        else:
            k += 1
    return i, j

def doPartitioning(A, left, right, pivot):
    A[pivot], A[right] = A[right], A[pivot]

    cur = left
    for i, x in enumerate(A[left:right]):
        if x < A[right]:
            A[i + left], A[cur] = A[cur], A[i + left]
            cur += 1
    A[cur], A[right] = A[right], A[cur]
    return cur


def leftPivot(A, left, right):
    return left


def medianOfThreePivot(A, left, right):
    # Find the median of the left, mid, and right values
    mid = (left + right) // 2
    if A[left] <= A[mid] and A[mid] <= A[right] or A[right] <= A[mid] and A[mid] <= A[left]:
        pivot = mid
    elif A[mid] <= A[left] and A[left] <= A[right] or A[right] <= A[left] and A[left] <= A[mid]:
        pivot = left
    else:
        pivot = right
    return pivot

