"""
Michael Josten
Danielle Lambion
TCSS 598: Simulation of Sorting Techniques

This module will read the csv files collected by the tests of the sorting algorithms
and will create 4 graphs per csv file.

Each graph will contain the data of 5 different sorting algorithms.

Graph 1: X = size of data, y = algorithm runtime
Graph 2: X = size of data, y = amount of memory used
Graph 3: X = degree of sortedness, y = algorithm runtime
Graph 4: X = degree of sortedness, y = amount of memory used
"""

import matplotlib.pyplot as plt
import csv

NORM_RAND_DIST_PATH = "results/NormalRandomDistributionResults.csv"
UNIF_RAND_DIST_PATH = "results/UniformRandomDistributionResults.csv"
INC_CREDIT_DEFAULT_PATH = "results/IncomeForCreditCardDefaultDatasetResults.csv"
AVG_EARNING_PATH = "results/AverageEarningsDatasetResults.csv"

def main():
    plotData(NORM_RAND_DIST_PATH, "Random Normal Distribution Dataset", 25000, 153000000, 60, 18)
    plotData(UNIF_RAND_DIST_PATH, "Random Uniform Distribution Dataset", 25000, 155000000, 60, 18)
    plotData(INC_CREDIT_DEFAULT_PATH, "Income For Credit Card Default Dataset", 10000, 24600000, 10, 16)
    plotData(AVG_EARNING_PATH, "Average Hourly Earning Dataset", 12000, 31240000, 12, 17)
    


"""
Will read the input csv and for each line of data, will seperate 
each sorting algorithms runtime and memory usage. Will plot the 4 different graphs
for the csv file
@param inputPath is the input path to the csv file containing the sorting data
"""
def plotData(inputPath, title, dataSizeLim, sortednessLim, runtimeLim, footprintLim):

    dataSize = []
    sortedness = []
    runtimeDict = {"bubble":[], "selection":[], "insertion":[], "mergesort":[], "quicksort":[]}
    footprintDict = {"bubble":[], "selection":[], "insertion":[], "mergesort":[], "quicksort":[]}
    sortData(inputPath, dataSize, sortedness, runtimeDict, footprintDict)

    figs, axs = plt.subplots(2, 2, figsize=(8,8))
    figs.suptitle(title, fontsize=16)

    plotSubplot(axs[0,0], dataSize, runtimeDict, "Size of Data", "Runtime", "Runtime on Data Size", [10, dataSizeLim], [0, runtimeLim])
    plotSubplot(axs[0,1], dataSize, footprintDict, "Size of Data", "Footprint", "Footprint on Data Size", [10, dataSizeLim])#, [14, footprintLim])
    plotSubplot(axs[1,0], sortedness, runtimeDict, "Sortedness", "Runtime", "Runtime on Sortedness", [0, sortednessLim], [0, runtimeLim])
    plotSubplot(axs[1,1], sortedness, footprintDict, "Sortedness", "Footprint", "Footprint on Sortedness", [0, sortednessLim])#, [14, footprintLim])

    axs[0,0].legend(["Bubble Sort", "Selection Sort", "Insertion Sort", "MergeSort", "QuickSort"], loc='best')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Function that will plot the subplots based on the x list and the y dictionary
def plotSubplot(ax, xList, yDict, xLabel, yLabel, title, xlim=[0,0], ylim=[0,0]):
    color = ['r-', 'b-', 'g-', 'c-', 'y-']
    for i, key in enumerate(yDict.keys()):
        ax.plot(xList, yDict[key], color[i])
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    if not (xlim[0] == 0 and xlim[1] == 0):
        ax.set_xlim(xlim)
    if not (ylim[0] == 0 and ylim[1] == 0):
        ax.set_ylim(ylim)

    
# Function that will iterate through the csv file and will populate the lists and 
# dictionaries passed with data from each column.
def sortData(inputPath, dataSize, sortedness, runtimeDict, footprintDict):
    with open(inputPath, 'r') as input:
        input.readline()
        reader = csv.reader(input, delimiter=",")
        
        # sort data into lists
        for row in reader:
            dataSize.append(int(row[0]))
            sortedness.append(int(row[1]))
            #bubble sort data
            runtimeDict["bubble"].append(float(row[2]))
            footprintDict["bubble"].append(float(row[3]))
            #selection sort
            runtimeDict["selection"].append(float(row[4]))
            footprintDict["selection"].append(float(row[5]))
            #insertion sort
            runtimeDict["insertion"].append(float(row[6]))
            footprintDict["insertion"].append(float(row[7]))
            #mergesort
            runtimeDict["mergesort"].append(float(row[8]))
            footprintDict["mergesort"].append(float(row[9]))
            #quicksort
            runtimeDict["quicksort"].append(float(row[10]))
            footprintDict["quicksort"].append(float(row[11]))



if __name__ == "__main__":
    main()