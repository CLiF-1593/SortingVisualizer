import time

from SortingAlgorithm.Sort import ArrayType
from SortingAlgorithm.Bubble_Sort import BubbleSort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Selection_Sort import SelectionSort
from SortingAlgorithm.Quick_Sort import QuickSort
from SortingAlgorithm.Merge_Sort import MergeSort
from SortingAlgorithm.Shell_Sort import ShellSort

if __name__ == '__main__':
    sort = ShellSort()
    sort.SetArray(100, ArrayType.RANDOM)
    sort.SetSpeed(0.01)
    sort.SetPlaysound(True)
    sort.Sort()
    while not sort.IsFinished():
        time.sleep(0.016)