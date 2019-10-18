"""
Michael Josten
Danielle Lambion

TCSS 598 Masters Seminar
Simulation of Sorting Techniques Project:

This program will contain the 5 different sorting algorithms used by the project to 
test each algorithms runtime and memory footprint (x-axis) on data size and degree of sortedness
"""

import math
import random


def main():
    #test
    with open("NormalRandomDistribution.csv", 'r') as NormDistFile:
        NormDistFile.readline()
        A = []
        for line in NormDistFile.readlines():
            A.append(int(line.strip(" \n\t")))
    #A = [4, 5, 2, 6, 3, 6, -1, -2]
    print(len(A))
    print(A[:10])
    R = QuickSort(A)
    print("Original = {}...{}".format(A[:5], A[-5:]))
    print("Sorted = {}...{}".format(R[:5], R[-5:]))

"""
BubbleSort sorting algorithm will sort a list A by repeatedly swapping 
elements of the list A if the elements are out of order.
Swap el at j and j+1 if j+1 is bigger
Runtime is O(n^2)
extra space is O(1)
@param list of integers A
@return sorted list of integers
"""
def BubbleSort(A):
    R = A.copy()
    for i in range(len(R)):
        for j in range(len(R)-i-1):
            if R[j] > R[j+1]:
                temp = R[j]
                R[j] = R[j+1]
                R[j+1] = temp
    return R

"""
SelectionSort Sorting algorithm will find the minimum element, and swap its position with 
the first element in the array. The sorted subarray index will increase and the unsorted subarray 
index will increase. There will be a subarray which is sorted and a subarray which is unsorted.
Runtime is O(n^2)
extra space is O(1)
@param list of integers A
@return sorted list of integers
"""
def SelectionSort(A):
    R = A.copy()
    for i in range(len(R)-1):
        minIndex = i
        # Find the minimum index in the unsorted array
        for j in range(i+1, len(R)):
            if R[j] < R[minIndex]:
                minIndex = j
        # Swap the minimum index and the first element in the unsorted array.
        # Then increment the index of the sorted and unsorted array by 1
        temp = R[minIndex]
        R[minIndex] = R[i]
        R[i] = temp
    return R

"""
InsertionSort Sorting algorithm will pick element i and put it into its sorted place in
the array from R[0,..,i-1]. When element i is chose, increment the position of elements 0 to i-1
that are greater than i. then place i in the slot left open. There will be a subarray of 
sorted elements and a subarray of unsorted elements.
Runtime is O(n^2)
extra space is O(1)
@param list of integers A
@return sorted list of integers
"""
def InsertionSort(A):
    R = A.copy()
    for i in range(1, len(R)):
        tempI = R[i]
        j = i - 1
        # move elements that are greater than R[i] to the right one
        while j >= 0 and R[j] > tempI:
            R[j+1] = R[j]
            j -= 1
        R[j+1] = tempI
    return R

"""
MergeSort sorting algorithm. uses divide and conquer techniques to sort list of elements.
Recursively splits list into halves then merges the halves when they have reached a base case of 
one element per array. When merging, will have a left array index and a right array index, and will
build a sorted array by finding the smaller element of the left array index or the right array index and 
appending that element to the sorted merging list.
Runtime is O(n logn)
extra space is O(n)
"""
def MergeSort(A):
    R = A.copy()
    return __helpMergeSort(R)

def __helpMergeSort(A):
    if (len(A) > 1):
        m = math.floor(len(A) / 2)
        L = A[:m]
        R = A[m:]
        # recursively split list into halves
        MergeSort(L)
        MergeSort(R)
        # create left, right, and R indexes
        i = 0
        j = 0
        k = 0

        # merge left and right to R array
        while i < len(L) and j < len(R):
            if (L[i] < R[j]):
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        
        # merge rest of elements if any
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A

"""
QuickSort sorting algorithm involves choosing an element as a pivot and to 
split the list of elements before the pivot and after. We will be choosing the last element 
for the pivot element. Then recursing with the left and right array from the pivot
Worst Case Runtime is O(n^2)
Average Case Runtime is O(n log n)
Extra space is O(1)
@param A is a list of integers
@return a sorted list of integers
"""
def QuickSort(A):
    R = A.copy()
    return __helpQuickSort(R, 0, len(R)-1)

#helper function for quicksort recursion
# low and high are indexes of starting and ending indexes of A
def __helpQuickSort(A, low, high):
    if (low < high):
        partitionIndex = __partition(A, low, high)
        #A[partitionIndex] will be sorted
        __helpQuickSort(A, low, partitionIndex - 1)
        __helpQuickSort(A, partitionIndex + 1, high)
    return A

# Helper function for quicksort partition
# place pivot element in 
# correct position and place all smaller than pivot elements to left of pivot
# and all greater than pivot elements to right of pivot
def __partition(A, low, high):
    pivot = A[high]
    # index of the smaller elements
    i = low - 1

    for j in range(low, high):
        # check if current element is smaller than the pivot
        if A[j] < pivot:
            i += 1
            # swap the current element and the element at the index of the small elements
            A[i], A[j] = A[j], A[i]
    
    # after checking all elements for a elements that are smaller than the pivot
    # Swap to make the pivot in the correct location in the array which is after 
    # the smaller elements.
    A[i+1], A[high] = A[high], A[i+1]
    return (i + 1)

if __name__ == "__main__":
    main()