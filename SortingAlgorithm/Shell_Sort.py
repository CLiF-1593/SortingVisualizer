# =================================================================
# [GPL 2.0 License]
# Copyright (C) 2023 CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class ShellSort(Sort):
    def SortingProcess(self):
        g = len(self.arr)
        while g != 1:
            g = (g + 1) // 2
            for i in range(g, len(self.arr)):
                self.Step(comparing_index=[i], sound=i)
                while i >= g and self.arr[i - g] > self.arr[i]:
                    self.Step(comparing_index=[i - g, i], sound=i-g)
                    self.arr[i], self.arr[i - g] = self.arr[i - g], self.arr[i]
                    self.Step(comparing_index=[i - g, i], sound=i-g)
                    i -= g