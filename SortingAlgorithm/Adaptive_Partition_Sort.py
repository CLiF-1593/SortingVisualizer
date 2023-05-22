import math

from Sort import Sort
from Merge_Sort import MergeSort
from Insertion_Sort import InsertionSort

PIVOT = "FIRST"

class AdaptivePartitionSort(Sort):
    def SortingProcess(self):
        depth = int(math.log2(len(self.arr)))
        self.intro(0, len(self.arr)-1, depth)

    def intro(self, begin, end, depth):
        if end - begin + 1 <= math.log2(len(self.arr)):
            insertion_sort = InsertionSort(self.timer)
            insertion_sort.Copy(self)
            insertion_sort.SortingProcess(begin, end)
            return
        if depth == 0 :
            merge_sort = MergeSort(self.timer)
            merge_sort.Copy(self)
            merge_sort.SortingProcess(begin, end)
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
        self.intro(begin, pivot - 1, depth - 1)
        self.intro(pivot + 1, end, depth - 1)
