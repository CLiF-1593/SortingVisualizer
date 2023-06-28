# =================================================================
# [GPL 3.0 License]
# Copyright (C) 2023 by CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class RadixSort(Sort):
    unit : int

    def __init__(self, timer):
        Sort.__init__(self, timer)
        self.unit = 4

    def SetUnit(self, unit : int):
        if unit > 0:
            self.unit = unit

    def SortingProcess(self):
        digit = 1
        buf = [[] for i in range(self.unit)]
        max_digit = 1
        while self.max_data % max_digit != self.max_data:
            max_digit *= self.unit
        while digit != max_digit:
            buf = [[] for i in range(self.unit)]
            for i in range(len(self.arr)):
                index = (self.arr[i] // digit) % self.unit
                buf[index].append(self.arr[i])
                self.Step(comparing_index=[i], sound = i)
            index = 0
            for i in range(self.unit):
                for j in range(len(buf[i])):
                    self.arr[index] = buf[i][j]
                    self.Step(comparing_index=[index], sound=index)
                    index += 1
            digit *= self.unit