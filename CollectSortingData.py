"""
Michael Josten
Danielle Lambion
TCSS 598: Masters Seminar

Simulation of Sorting Algorithms Project:
Using 4 different data sets, will create a different csv files for each data set
which will each contain:
1. Size of Data
This will be the size of the array of integers used to test each sorting algorithm
2. Degree of Sortedness
Calculate degree of sortedness each time the size of the data increases for plotting a graph
3. Bubble Sort Runtime
4. Bubble Sort Footprint
The amount of memory that bubble sort needs to use
5. Selection Sort Runtime
6. Selection Sort Footprint
7. Insertion Sort Runtime
8. Insertion Sort Footprint
9. MergeSort Runtime
10. MergeSort Footprint
11. QuickSort Runtime
12. QuickSort Footprint

We will have a Random Normal Distribution set of 20,000 numbers. with mean of 50 
and standard deviation of 30

For each data set, we will start at a low number of data from that set, then increment 
the data usage by 100 or 300 or whichever amount is most appropriate. Each time the data
size increments, we will run each algorithm 5 times and collect the average runtime and 
footprint to record the result with. 

Using the csv files, we will plot 16 graphs total. 4 from each csv file containing each
sorting algorithm data.
Graph 1: X = Size of Data, Y = Algorithm Runtime
Graph 2: X = Size of Data, Y = Algorithm Footprint (memory used)
Graph 3: X = Degree of Sortedness, Y = Algorithm Runtime
Graph 4: X = Degree of Sortedness, Y = Algorithm Footprint
Plotting graphs will be in a different module, it is just described here

TODO: If need something between 0-1 for sortedness can look at Spearman Correleation Coefficient

"""

#imports
import time
from memory_profiler import memory_usage
from SortingAlgorithms import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort

NORM_RAND_DIST_SET = "NormalRandomDistribution.csv"
NORM_RAND_DIST_OUTPUT = "NormalRandomDistributionResults.csv"


# Main driver function for the data collection program
def main():
    # A = [6, 5, 4, 3, 2, 1]
    # print("{:.6f}".format(CalcSortedness(A)))
    collectSortingData(NORM_RAND_DIST_SET, NORM_RAND_DIST_OUTPUT)


# Function that takes the input path of the data, performs the experiments described
# and outputs the results to the outputPath file.
def collectSortingData(inputPath, outputPath):
    A = []
    # open input file and extract data set
    with open(inputPath, 'r') as input:
        input.readline()
        for line in input.readlines():
            # collect array of data
            A.append(int(line.strip(" \n\t")))
    
    # increment the size of the data by 100
    # for i in range(10, len(A), 100):
    #     testA = A[:i]
    #     sizeOfData = len(testA)
    #     sortedness = CalcSortedness(testA)
    #     bubbleStartTime = time.perf_counter()
    testA = A[:100]
    sizeOfData = len(testA)
    sortedness = CalcSortedness(testA)
    bubbleStartTime = time.perf_counter()
    bubbleFootprint = memory_usage((BubbleSort, [testA]), max_usage=True)
    bubbleRunTime = (time.perf_counter() - bubbleStartTime)
    print("Size of Data = {}".format(sizeOfData))
    print("Measure of Sortedness = {}".format(sortedness))
    print("BubbleSort Runtime = {}".format(bubbleRunTime))
    print("Bubble Footprint = {}".format(bubbleFootprint))
    

        
"""
A measure of sortedness could be the number of inversions. This is the number
of swaps it would take to sort an array.
"""
def CalcSortedness(A):
    inversionCount = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if (A[i] > A[j]):
                inversionCount += 1
    return inversionCount 


if __name__ == "__main__":
    main()