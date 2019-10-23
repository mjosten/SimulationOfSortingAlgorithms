CollectSortingData.py will run each of the sorting algorithms 5 times when the size of the dataset increases by 100. Then collects the runtime and the memory foot print and averages those 5 runs. The results are collected and written to a .csv results file

PlotData.py when run will plot 4 graphs for each of the datasets based on the .csv files created by CollectSortingData.py

SortingAlgorithms.py is a module that contains the 5 sorting algorithms.

Packages Required to Run
- memory_profiler
- matplotlib