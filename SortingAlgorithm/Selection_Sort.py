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