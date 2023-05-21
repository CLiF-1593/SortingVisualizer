from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Merge_Sort import MergeSort

THRESHOLD = 32

class TimSort(Sort):
    def SortingProcess(self):
        insertion_sort = InsertionSort(self.timer)
        insertion_sort.delay = self.delay
        insertion_sort.playsound = self.playsound
        insertion_sort.pivot = self.pivot
        insertion_sort.comparing = self.comparing
        insertion_sort.partition = self.partition
        insertion_sort.check = self.check
        for i in range(len(self.arr) // THRESHOLD + 1):
            insertion_sort.SetArrayDirectly(self.arr)
            insertion_sort.SortingProcess(i * THRESHOLD, min((i + 1) * THRESHOLD + 1, len(self.arr) - 1))
        level = THRESHOLD
        merge_sort = MergeSort(self.timer)
        merge_sort.delay = self.delay
        merge_sort.playsound = self.playsound
        merge_sort.pivot = self.pivot
        merge_sort.comparing = self.comparing
        merge_sort.partition = self.partition
        while level < len(self.arr):
            for i in range(0, len(self.arr) - level, level * 2):
                begin = i
                mid = i + level - 1
                end = min(begin + level * 2 - 1, len(self.arr) - 1)
                merge_sort.SetArrayDirectly(self.arr)
                merge_sort.Merge(begin, mid, end)
            level *= 2
