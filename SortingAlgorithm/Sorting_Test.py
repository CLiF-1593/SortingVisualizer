from SortingAlgorithm.Sort import ArrayType
from SortingAlgorithm.Bubble_Sort import BubbleSort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Selection_Sort import SelectionSort
from SortingAlgorithm.Quick_Sort import QuickSort
from SortingAlgorithm.Merge_Sort import MergeSort
from SortingAlgorithm.Shell_Sort import ShellSort
from SortingAlgorithm.Radix_Sort import RadixSort
from SortingAlgorithm.Heap_Sort import HeapSort
from SortingAlgorithm.CombSort import CombSort
from SortingAlgorithm.Counting_Sort import CountingSort
from SortingAlgorithm.Tim_Sort import TimSort
from SortingAlgorithm.Intro_Sort import IntroSort
from SortingAlgorithm.Bogo_Sort import BogoSort
from SortingAlgorithm.Odd_Even_Sort import OddEvenSort
from SortingAlgorithm.Gnome_Sort import GnomeSort

import time

if __name__ == '__main__':
    sort = GnomeSort()
    sort.SetArray(50, 1, ArrayType.RANDOM)
    sort.SetSpeed(0.01)
    sort.SetPlaysound(True)
    sort.Sort()
    while not sort.IsFinished():
        time.sleep(0.016)