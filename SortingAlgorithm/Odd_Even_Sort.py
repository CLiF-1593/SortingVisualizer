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

class OddEvenSort(Sort):
    def SortingProcess(self):
        change = True
        while change:
            change = False
            for i in range(1, len(self.arr) - 1, 2):
                self.Step(comparing_index=[i], sound=i)
                self.Step(comparing_index=[i + 1], sound=i + 1)
                if self.arr[i] > self.arr[i + 1]:
                    self.Step(comparing_index=[i, i + 1], sound=i)
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    change = True
                    self.Step(comparing_index = [i, i+1], sound=i)
            for i in range(0, len(self.arr) - 1, 2):
                self.Step(comparing_index=[i], sound=i)
                self.Step(comparing_index=[i + 1], sound=i + 1)
                if self.arr[i] > self.arr[i + 1]:
                    self.Step(comparing_index=[i, i + 1], sound=i)
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    change = True
                    self.Step(comparing_index = [i, i+1], sound=i)
            if not change:
                break