import math

from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Heap_Sort import HeapSort
from SortingAlgorithm.Insertion_Sort import InsertionSort

PIVOT = "FIRST"

class IntroSort(Sort):
    def SortingProcess(self):
        depth = int(math.log2(len(self.arr)))
        self.intro(0, len(self.arr)-1, depth)

    def intro(self, begin, end, depth):
        if end - begin + 1 <= 16:
            insertion_sort = InsertionSort(self.timer)
            insertion_sort.delay = self.delay
            insertion_sort.SetPlaysound(self.playsound)
            insertion_sort.SetArrayDirectly(self.arr)
            insertion_sort.SortingProcess(begin, end)
            return
        if depth == 0 :
            heap_sort = HeapSort(self.timer)
            heap_sort.delay = self.delay
            heap_sort.SetPlaysound(self.playsound)
            heap_sort.SetArrayDirectly(self.arr)
            heap_sort.SortingProcess(begin, end)
            return
        if PIVOT == "FIRST":
            pivot = begin
        else:
            pivot = end
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
