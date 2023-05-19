import time

from SortingAlgorithm.Sort import ArrayType
from SortingAlgorithm.Bubble_Sort import BubbleSort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Selection_Sort import SelectionSort

if __name__ == '__main__':
    sort = SelectionSort()
    sort.SetArray(50, ArrayType.RANDOM)
    sort.SetSpeed(0.01)
    sort.SetPlaysound(True)
    sort.Sort()
    while not sort.IsFinished():
        time.sleep(0.016)