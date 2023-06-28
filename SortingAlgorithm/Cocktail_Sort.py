# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class CocktailSort(Sort):
    def SortingProcess(self):
        start_index = 0
        last_index = len(self.arr) - 1
        while start_index < last_index:
            change_index = last_index
            for j in (range(start_index, last_index)):
                self.Step(comparing_index=[j], sound=j)
                self.Step(comparing_index=[j + 1], sound=j + 1)
                if self.arr[j] > self.arr[j + 1]:
                    self.Step(comparing_index=[j, j + 1], sound=j)
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    change_index = j
                    self.Step(comparing_index = [j, j+1], sound=j)
            if change_index == last_index:
                break
            last_index = change_index
            change_index = start_index
            for j in (range(last_index, start_index, -1)):
                self.Step(comparing_index=[j], sound=j)
                self.Step(comparing_index=[j - 1], sound=j - 1)
                if self.arr[j] < self.arr[j - 1]:
                    self.Step(comparing_index=[j, j - 1], sound=j)
                    self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                    change_index = j
                    self.Step(comparing_index=[j, j - 1], sound=j)
            if change_index == start_index:
                break
            start_index = change_index