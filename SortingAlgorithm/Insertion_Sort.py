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

class InsertionSort(Sort):
    def SortingProcess(self, begin = None, end = None):
        partition = []
        if begin == None :
            begin = 0
            end = len(self.arr) - 1
        else:
            partition = [begin, end]
        for i in range(begin + 1, end + 1):
            self.Step(comparing_index=[i], sound=i, partition = partition)
            while i > begin and self.arr[i - 1] > self.arr[i]:
                self.Step(comparing_index=[i - 1, i], sound=i-1, partition = partition)
                self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                self.Step(comparing_index=[i - 1, i], sound=i-1, partition = partition)
                i -= 1