from enum import Enum

from SortingAlgorithm.Sort import Sort

class QuickSort(Sort):
    class PivotType(Enum):
        PIVOT_FIRST = 0
        PIVOT_LAST = 1

    type : PivotType

    def __init__(self, timer):
        Sort.__init__(self, timer)
        self.type = QuickSort.PivotType.PIVOT_FIRST

    def SetPivot(self, type : PivotType):
        self.type = type

    def _pivot(self, first, last):
        if self.type == QuickSort.PivotType.PIVOT_FIRST:
            return first
        return last

    def SortingProcess(self, begin = 0, end = None):
        if end == None: end = len(self.arr) - 1
        if begin >= end : return
        pivot = self._pivot(begin, end)
        self.Step(comparing_index = [pivot], sound = pivot)
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

        if self.type == QuickSort.PivotType.PIVOT_FIRST:
            self.Step(comparing_index=[pivot, right], partition = [begin, end], sound=pivot)
            self.arr[pivot], self.arr[right] = self.arr[right], self.arr[pivot]
            self.Step(comparing_index=[pivot, right], partition = [begin, end], sound=pivot)
            pivot = right
        else:
            self.Step(comparing_index=[pivot, left], partition = [begin, end], sound=pivot)
            self.arr[pivot], self.arr[left] = self.arr[left], self.arr[pivot]
            self.Step(comparing_index=[pivot, left], partition = [begin, end], sound=pivot)
            pivot = left
        self.SortingProcess(begin, pivot - 1)
        self.SortingProcess(pivot + 1, end)