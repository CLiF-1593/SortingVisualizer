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