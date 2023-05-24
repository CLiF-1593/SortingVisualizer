# =================================================================
# [GPL 2.0 License]
# Copyright (C) 2023 CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class SelectionSort(Sort):
    def SortingProcess(self):
        for i in range(0, len(self.arr) - 1):
            min = self.arr[i]
            index = i
            self.Step(comparing_index=[index], sound=index)
            for j in range(i + 1, len(self.arr)):
                self.Step(pivot = i, comparing_index = [j, index], sound=j)
                if min > self.arr[j]:
                    min = self.arr[j]
                    index = j
                    self.Step(pivot=i, comparing_index=[index], sound=index)
            self.arr[i], self.arr[index] = self.arr[index], self.arr[i]
            self.Step(comparing_index=[i, index], sound=index)