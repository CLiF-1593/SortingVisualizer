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
