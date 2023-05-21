from Sort import ArrayType
from Bubble_Sort import BubbleSort
from Insertion_Sort import InsertionSort
from Selection_Sort import SelectionSort
from Quick_Sort import QuickSort
from Merge_Sort import MergeSort
from Shell_Sort import ShellSort
from Radix_Sort import RadixSort
from Heap_Sort import HeapSort
from CombSort import CombSort
from Counting_Sort import CountingSort
from Tim_Sort import TimSort
from Intro_Sort import IntroSort
from Bogo_Sort import BogoSort
from Odd_Even_Sort import OddEvenSort
from Gnome_Sort import GnomeSort

import time
from SylTimer import SylTimer

if __name__ == '__main__':
    timer = SylTimer()

    sort = RadixSort(timer)
    sort.SetArray(999, 1, ArrayType.RANDOM)
    sort.SetSpeed(0.01)
    sort.SetPlaysound(True)
    timer.zero()
    sort.Sort()
    while not sort.IsFinished():
        time.sleep(0.016)