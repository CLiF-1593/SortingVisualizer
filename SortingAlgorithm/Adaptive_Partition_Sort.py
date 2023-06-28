# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

# Adaptive Partition Sort (APS)
# Developed by ryankwondev, shiueo, sat0317, CLiF and krrrr0
# Original Source Github : https://github.com/ryankwondev/Adaptive-Partition-Sort

import math

from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Tim_Sort import TimSort
from SortingAlgorithm.Insertion_Sort import InsertionSort

PIVOT = "FIRST"
class AdaptivePartitionSort(Sort):
    def SortingProcess(self):
        depth = int(math.log2(len(self.arr)))
        self.aps(0, len(self.arr)-1, depth)

    def aps(self, begin, end, depth):
        if end - begin + 1 <= 16:
            insertion_sort = InsertionSort(self.timer)
            insertion_sort.Copy(self)
            insertion_sort.SortingProcess(begin, end)
            return
        if depth == 0 :
            # Merge + Insertion -> Tim
            tim_sort = TimSort(self.timer)
            tim_sort.Copy(self)
            tim_sort.SortingProcess(begin, end)
            return
        if PIVOT == "FIRST":
            pivot = begin
        else:
            pivot = end
        self.Step(comparing_index = [pivot], sound = pivot, partition = [begin, end])
        left = begin
        right = end
        self.Step(comparing_index=[left, right], pivot = pivot, partition = [begin, end], sound = right if left == pivot else left)
        while left < right:
            while left < end and self.arr[left] <= self.arr[pivot]:
                left += 1
                self.Step(comparing_index=[left, right], pivot=pivot, partition = [begin, end], sound=left)
            while right > begin and self.arr[right] >= self.arr[pivot]:
                right -= 1
                self.Step(comparing_index=[right, left], pivot=pivot, partition = [begin, end], sound=right)
            if left < right:
                self.Step(comparing_index=[left, right], pivot=pivot, partition = [begin, end], sound=left)
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                self.Step(comparing_index=[left, right], pivot=pivot, partition = [begin, end], sound=left)

        if PIVOT == "FIRST":
            self.Step(comparing_index=[pivot, right], partition = [begin, end], sound=pivot)
            self.arr[pivot], self.arr[right] = self.arr[right], self.arr[pivot]
            self.Step(comparing_index=[pivot, right], partition = [begin, end], sound=pivot)
            pivot = right
        else:
            self.Step(comparing_index=[pivot, left], partition = [begin, end], sound=pivot)
            self.arr[pivot], self.arr[left] = self.arr[left], self.arr[pivot]
            self.Step(comparing_index=[pivot, left], partition = [begin, end], sound=pivot)
            pivot = left
        self.aps(begin, pivot - 1, depth - 1)
        self.aps(pivot + 1, end, depth - 1)
