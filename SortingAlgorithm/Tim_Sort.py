from Sort import Sort
from Insertion_Sort import InsertionSort
from Merge_Sort import MergeSort

THRESHOLD = 16

class TimSort(Sort):
    def SortingProcess(self):
        insertion_sort = InsertionSort(self.timer)
        insertion_sort.Copy(self)
        for i in range(len(self.arr) // THRESHOLD + 1):
            insertion_sort.SortingProcess(i * THRESHOLD, min((i + 1) * THRESHOLD - 1, len(self.arr) - 1))
        level = THRESHOLD
        merge_sort = MergeSort(self.timer)
        merge_sort.Copy(self)
        while level < len(self.arr):
            for i in range(0, len(self.arr) - level, level * 2):
                begin = i
                mid = i + level - 1
                end = min(begin + level * 2 - 1, len(self.arr) - 1)
                merge_sort.Merge(begin, mid, end)
            level *= 2
