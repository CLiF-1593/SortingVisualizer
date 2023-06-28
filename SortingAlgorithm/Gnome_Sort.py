# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class GnomeSort(Sort):
    def SortingProcess(self):
        pos = 0
        while pos < len(self.arr):
            if pos == 0 or self.arr[pos] >= self.arr[pos - 1]:
                if pos == 0: self.Step(comparing_index=[pos], sound = pos)
                else: self.Step(comparing_index=[pos, pos - 1], sound = pos)
                pos += 1
            else:
                self.Step(comparing_index=[pos, pos - 1], sound=pos)
                self.arr[pos], self.arr[pos - 1] = self.arr[pos - 1], self.arr[pos]
                self.Step(comparing_index=[pos, pos - 1], sound=pos)
                pos -= 1