# Copyright (C) 2023 CLiF and Syeosle
#
# [MIT License]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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