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

Datasets:
1. We will have a Random Normal Distribution set of 25,000 numbers. with mean of 50 
and standard deviation of 30
2. Income when invidvidual defaults on a credit card dataset. 10000 decimal numbers.
3. Average earning data set. 11130 numbers
4. Uniform Random Distribution set of 25,000 decimal numbers from 0 to 100


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

The Runtime of an algorithm is displayed as fractional seconds. 
- For examples: 1.33 fracional seconds = 1 second and 330 milliseconds TODO find out if this is true
The Data used will be in MB (MegaBytes) TODO or can be in Asymptotic size if we need to change is


TODO: If need something between 0-1 for sortedness can look at Spearman Correleation Coefficient

"""

#imports
import time
from memory_profiler import memory_usage
from SortingAlgorithms import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort

#NormalRandomDistribution
NORM_RAND_DIST_SET = "datasets/NormalRandomDistribution.csv"
NORM_RAND_DIST_OUTPUT = "results/NormalRandomDistributionResults.csv"
#UniformRandomDistribution
UNIF_RAND_DIST_SET = "datasets/UniformRandomDistribution.csv"
UNIF_RAND_DIST_OUTPUT = "results/UniformRandomDistributionResults.csv"
#AverageEarningDataset
AVG_EARN_DATASET = "datasets/AverageEarningsDataset.csv"
AVG_EARN_OUTPUT = "results/AverageEarningsDatasetResults.csv"
#IncomeForCreditCardDefaultDataset
INC_CREDIT_DEFAULT_DATASET = "datasets/IncomeForCreditCardDefaultDataset.csv"
INC_CREDIT_DEFAULT_OUTPUT = "results/IncomeForCreditCardDefaultDatasetResults.csv"


# Main driver function for the data collection program
def main():
    #collectSortingData(NORM_RAND_DIST_SET, NORM_RAND_DIST_OUTPUT)
    # collectSortingData(UNIF_RAND_DIST_SET, UNIF_RAND_DIST_OUTPUT)
    # collectSortingData(AVG_EARN_DATASET, AVG_EARN_OUTPUT)
    collectSortingData(INC_CREDIT_DEFAULT_DATASET, INC_CREDIT_DEFAULT_OUTPUT)

# Function that takes the input path of the data, performs the experiments described
# and outputs the results to the outputPath file.
def collectSortingData(inputPath, outputPath):
    print("Starting: {}".format(inputPath))
    A = []
    # open input file and extract data set
    with open(inputPath, 'r') as input:
        input.readline()
        for line in input.readlines():
            # collect array of data
            A.append(float(line.strip(" \n\t")))
    
    outputFile = open(outputPath, 'w+')
    setupCSV(outputFile)
    # increment the size of the data by 100
    #for i in range(10, len(A), 100):
    for i in range(10, len(A), 100):
        testA = A[:i]
        sizeOfData = len(testA)
        sortedness = CalcSortedness(testA)

        runtimeDict = {"bubble":0, "selection":0, "insertion":0, "mergesort":0, "quicksort":0}
        footprintDict = {"bubble":0, "selection":0, "insertion":0, "mergesort":0, "quicksort":0}

        for _ in range(5):
            # Run each sorting algorithm over test list A
            bubbleRuntime, bubbleFootprint = testSorting(testA, BubbleSort)
            selectionRuntime, selectionFootprint = testSorting(testA, SelectionSort)
            insertionRuntime, insertionFootprint = testSorting(testA, InsertionSort)
            mergesortRuntime, mergesortFootprint = testSorting(testA, MergeSort)
            quicksortRuntime, quicksortFootprint = testSorting(testA, QuickSort)
            
            #Calculate sums of the runtimes and footprints
            #bubble
            runtimeDict["bubble"] += bubbleRuntime
            footprintDict["bubble"] += bubbleFootprint[0]
            #selection
            runtimeDict["selection"] += selectionRuntime
            footprintDict["selection"] += selectionFootprint[0]
            #insertion
            runtimeDict["insertion"] += insertionRuntime
            footprintDict["insertion"] += insertionFootprint[0]
            #mergesort
            runtimeDict["mergesort"] += mergesortRuntime
            footprintDict["mergesort"] += mergesortFootprint[0]
            #quicksort
            runtimeDict["quicksort"] += quicksortRuntime
            footprintDict["quicksort"] += quicksortFootprint[0]
        
        #average the runtimes and footprints
        for key in runtimeDict.keys():
            runtimeDict[key] = runtimeDict[key] / 5
            footprintDict[key] = footprintDict[key] / 5
        
        writeToOutput(outputFile, sizeOfData, sortedness, runtimeDict, footprintDict)
        print("Finished Data Size: {}".format(sizeOfData))
    
# Function that will write the results of a sorting test to the output file
def writeToOutput(output, dataSize, sortedness, runtimeDict, footprintDict):
#Size of Data, Degree of Sortedness, Bubble Runtime, Bubble Footprint, Selection Runtime, Selection Footprint, Insertion Runtime, Insertion Footprint, MergeSort Runtime, MergeSort Footprint, QuickSort Runtime, QuickSort Footprint
    data = "{}, {}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}\n".format(
        dataSize, sortedness, runtimeDict["bubble"], footprintDict["bubble"],
        runtimeDict["selection"], footprintDict["selection"], runtimeDict["insertion"], footprintDict["insertion"],
        runtimeDict["mergesort"], footprintDict["mergesort"], runtimeDict["quicksort"], footprintDict["quicksort"])
    output.write(data)

# Function that will write the data labels to the csv
def setupCSV(output):
    dataLabels = "Size of Data, Degree of Sortedness, Bubble Runtime, Bubble Footprint, Selection Runtime, Selection Footprint, Insertion Runtime, Insertion Footprint, MergeSort Runtime, MergeSort Footprint, QuickSort Runtime, QuickSort Footprint\n"
    output.write(dataLabels)

"""
Function that takes a array a, and a sorting algorithm sortF and will 
record runtime and data footprint of the sorting algorithm
"""
def testSorting(A, sortF):
    startTime = time.perf_counter()
    footPrint = memory_usage((sortF, [A]), max_usage=True)
    runTime = (time.perf_counter() - startTime)
    return runTime, footPrint
        
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

# function that sums all the elements of a list
def sumList(A):
    total = 0
    for el in A:
        total += el
    return total

if __name__ == "__main__":
    main()