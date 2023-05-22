# Copyright (C) 2023 CLiF and Syeosle
#
# [MIT License]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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