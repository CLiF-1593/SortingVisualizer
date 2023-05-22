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

from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Merge_Sort import MergeSort

THRESHOLD = 16

class TimSort(Sort):
    def SortingProcess(self, low = 0, high = -1):
        if high == -1: high = len(self.arr) - 1
        insertion_sort = InsertionSort(self.timer)
        insertion_sort.Copy(self)
        for i in range((high - low + 1) // THRESHOLD + 1):
            insertion_sort.SortingProcess(low + i * THRESHOLD, low + min((i + 1) * THRESHOLD - 1, high - low))
        level = THRESHOLD
        merge_sort = MergeSort(self.timer)
        merge_sort.Copy(self)
        while level <= high - low:
            for i in range(low, high + 1 - level, level * 2):
                begin = i
                mid = i + level - 1
                end = min(begin + level * 2 - 1, high)
                merge_sort.Merge(begin, mid, end)
            level *= 2
