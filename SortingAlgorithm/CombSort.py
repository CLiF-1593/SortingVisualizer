# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class CombSort(Sort):
    def SortingProcess(self):
        g = len(self.arr)
        while True:
            g = int((g - 1) / 1.3 + 1)
            change = False
            for j in range(len(self.arr) - g):
                self.Step(comparing_index=[j], sound=j)
                self.Step(comparing_index=[j + g], sound=j + g)
                if self.arr[j] > self.arr[j + g]:
                    self.Step(comparing_index=[j, j + g], sound=j)
                    self.arr[j], self.arr[j + g] = self.arr[j + g], self.arr[j]
                    change = True
                    self.Step(comparing_index = [j, j+g], sound=j)
            if not change and g == 1:
                break