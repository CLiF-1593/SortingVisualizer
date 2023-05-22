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