# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class InsertionSort(Sort):
    def SortingProcess(self, begin = None, end = None):
        partition = []
        if begin == None :
            begin = 0
            end = len(self.arr) - 1
        else:
            partition = [begin, end]
        for i in range(begin + 1, end + 1):
            self.Step(comparing_index=[i], sound=i, partition = partition)
            while i > begin and self.arr[i - 1] > self.arr[i]:
                self.Step(comparing_index=[i - 1, i], sound=i-1, partition = partition)
                self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                self.Step(comparing_index=[i - 1, i], sound=i-1, partition = partition)
                i -= 1