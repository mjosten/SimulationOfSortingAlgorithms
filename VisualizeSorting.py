"""
Michael Josten
Danielle Lambion
TCSS 598: Masters Seminar

Visualization of Sorting Algorithms

We will be showing how different sorting techniques perform given a set of data by 
creating a video that records the sorting process
Video needs:
1. Introduction frame that has names, date, and title.
2. brief description of the project: algorithm names and the datasets
3. Show all 5 sorting algorithms implemented by sorting at least 2 different types of datasets
- make sure that the graphs are labeled well
4. Analyze the results, which technique is better with which set and why.
- video cannot be more than 10 minutes
5. reference frame (if applicable)


The datasets used will 100 numbers each, 
1. randomly shuffled dataset
2. reverse order dataset

We will need to show the number of operations to sort each dataset with each sorting algorithm

NOTE: to run you need to download and install ffmpeg

TODO: get the rest of the videos and edit them together,
make sure that the video is less than 10 min.
"""

#imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import random
import math
import os.path as path


# Constants
DATASET_SIZE = 100
TITLE = "Quick Sort with Reverse Dataset"
FPS = 30
FILENAME = "QuickSortReverse.mp4"

# random dataset
# DATASET = [x + 1 for x in range(DATASET_SIZE)]
# random.shuffle(DATASET)

#Static random dataset
# inputFile = open("datasets/shuffledList.csv", "r")
# DATASET = inputFile.readline().strip("\t\n ").split(",")
# for i, x in enumerate(DATASET):
#     DATASET[i] = int(x)

#reverse order dataset.
DATASET = [x for x in range(DATASET_SIZE, 1, -1)]

"""
Main function for visualization project.
"""
def main():
    # define sorting function to use
    SORTING_FUNC = QuickSort

    
    # Initialize the figure and the axis for matplotlib subplots
    fig, ax = plt.subplots()
    ax.set_title(TITLE)
    # ax.set_ylabel("Number Value")

    #Formatting for movie files
    # writer = animation.FFMpegWriter(fps=20, metadata=dict(artist="Michael Josten and Danielle Lambion"),
    # bitrate=1800)
    Writer = animation.writers["ffmpeg"]
    writer = Writer(fps=FPS, metadata=dict(artist="Michael Josten and Danielle Lambion"), bitrate=1800)

    # initialize the bar graph
    # bar requires x axis and y axis, x will be the index of the number in the list
    # and y will be the value of the number
    bars = ax.bar(range(len(DATASET)), DATASET, align="edge")

    # text in the upper left corner to display the number of operations performed by the
    # sorting algorithm. Each time a sorting algorithm returns from a yield, it will
    # count as 1 operation
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Define the sort function generator
    sortFuncGen = SORTING_FUNC(DATASET)

    # for el in sortFuncGen:
    #     print(el)

    
    # define a function updateFigure to use with the matplotlib animation.
    # track the number of operations or number of iterations the animation as done.
    iteration = [0]
    # call the animation, sortFunc is the function called to process the dataset.
    anim = FuncAnimation(fig, func=updateFigure, fargs=(bars, iteration, text),
    frames=sortFuncGen, interval=1, repeat=False, save_count=10000)

    anim.save(path.join("visualizationVideos", FILENAME), writer=writer)

    # plt.show()

    print("done!")

# Function that will be called whenever we want to move a frame in the bar graph animation
def updateFigure(dataList, bars, iteration, text):
    for bar, value in zip(bars, dataList):
        bar.set_height(value)
    iteration[0] += 1
    text.set_text("Operations: {}".format(iteration[0]))
    

# create a generator for bubble sort which will give the value of the
# list passed after each iteration but save the current state of the function
# to be called again.
# repeatedly swap elements until the list is sorted.
def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
            yield A


# create a generator of the selection sort algorithm
# Find the minimum element and swap its position with the first element in the list.
def SelectionSort(A):
    for i in range(len(A)-1):
        minIndex = i
        # Find the minimum index in the unsorted array
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
                yield A
        # Swap the minimum index and the first element in the unsorted array.
        # Then increment the index of the sorted and unsorted array by 1
        temp = A[minIndex]
        A[minIndex] = A[i]
        A[i] = temp
        yield A

# create a generator of the insertion sort algorithm
# take the ith element and put it in its sorted place in the sorted subarray 
# then increment the subarray size by 1 and shrink the unsorted subarray
def InsertionSort(A):
    for i in range(1, len(A)):
        tempI = A[i]
        j = i - 1
        # move elements that are greater than A[i] to the right one
        while j >= 0 and A[j] > tempI:
            A[j+1] = A[j]
            j -= 1
            yield A
        A[j+1] = tempI
        yield A

# Divide and conquer technique to split the array in half and sort each side recursively.
def MergeSort(A):
    yield from __helpMergeSort(A, 0, len(A) - 1)

def __helpMergeSort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from __helpMergeSort(A, start, mid)
    yield from __helpMergeSort(A, mid+1, end)
    yield from __helpMerge(A, start, mid, end)
    yield A

# Helper function for merge sort to merge the L and R arrays into A
def __helpMerge(A, start, mid, end):
    merged = []
    leftIndex = start
    rightIndex = mid + 1

    # merge the left and the right sub arrays
    while leftIndex <= mid and rightIndex <= end:
        if A[leftIndex] < A[rightIndex]:
            merged.append(A[leftIndex])
            leftIndex += 1
        else:
            merged.append(A[rightIndex])
            rightIndex += 1

    # while any values left in Left, add to the merged array
    while leftIndex <= mid:
        merged.append(A[leftIndex])
        leftIndex += 1
    
    #while any values left in Right, add to the merged array
    while rightIndex <= end:
        merged.append(A[rightIndex])
        rightIndex += 1

    # set the values in A, the values of the merged array
    for i, sortedValue in enumerate(merged):
        A[start + i] = sortedValue
        yield A

# Quick Sort sorting algorithm with will partition the elements of the array on the 
# last element and sort both sides of the partition recursively
def QuickSort(A):
    yield from __helpQuickSort(A, 0, len(A) - 1)

# Helper method for quick sort which takes the start and end of the subarray 
# to use recursion
# Make the pivot element the end of the array
# If any element is smaller than the pivot, the swap the pivot and the element.
# and increment the pivot index
# Then swap the end element with the pivot
# recursively sort each side of the pivot.
def __helpQuickSort(A, start, end):
    if start >= end:
        return
    
    pivot = A[end]
    pivotIndex = start

    for i in range(start, end):
        if (A[i]) < pivot:
            A[i], A[pivotIndex] = A[pivotIndex], A[i]
            pivotIndex += 1
        yield A
    
    A[end], A[pivotIndex] = A[pivotIndex], A[end]
    yield A

    yield from __helpQuickSort(A, start, pivotIndex - 1)
    yield from __helpQuickSort(A, pivotIndex + 1, end)



if __name__ == "__main__":
    main()