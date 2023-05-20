from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Merge_Sort import MergeSort

THRESHOLD = 32

class TimSort(Sort):
    def SortingProcess(self):
        insertion_sort = InsertionSort()
        insertion_sort.SetSpeed(self.delay)
        insertion_sort.SetPlaysound(self.playsound)
        for i in range(len(self.arr) // THRESHOLD + 1):
            insertion_sort.SetArrayDirectly(self.arr)
            insertion_sort.SortingProcess(i * THRESHOLD, min((i + 1) * THRESHOLD + 1, len(self.arr) - 1))
        level = THRESHOLD
        merge_sort = MergeSort()
        merge_sort.SetSpeed(self.delay)
        merge_sort.SetPlaysound(self.playsound)
        while level < len(self.arr):
            for i in range(0, len(self.arr) - level, level * 2):
                begin = i
                mid = i + level - 1
                end = min(begin + level * 2 - 1, len(self.arr) - 1)
                merge_sort.SetArrayDirectly(self.arr)
                merge_sort.Merge(begin, mid, end)
            level *= 2
