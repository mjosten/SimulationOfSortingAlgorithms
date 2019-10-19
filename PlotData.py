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

import matplotlib as pl
import csv

NORM_RAND_DIST_PATH = "NormalRandomDistributionResults.csv"

def main():
    plotData(NORM_RAND_DIST_PATH)


"""
Will read the input csv and for each line of data, will seperate 
each sorting algorithms runtime and memory usage. Will plot the 4 different graphs
for the csv file
@param inputPath is the input path to the csv file containing the sorting data
"""
def plotData(inputPath):
    with open(inputPath, 'r') as input:
        input.readline()
        reader = csv.reader(input, delimiter=",")
        for row in reader:
            print(row)



if __name__ == "__main__":
    main()