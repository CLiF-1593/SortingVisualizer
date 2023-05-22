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

import math
from random import randrange

from SortingAlgorithm.Sort import Sort

class BogoSort(Sort):
    def Sorted(self):
        for i in range(len(self.arr) - 1):
            self.Step(comparing_index=[i, i + 1], sound = i)
            if self.arr[i] > self.arr[i + 1]:
                return False
        return True

    def Shuffle(self):
        for i in range(len(self.arr)-1):
            index = randrange(i, len(self.arr))
            self.Step(comparing_index=[i, index], sound=i)
            self.arr[index], self.arr[i] = self.arr[i], self.arr[index]
            self.Step(comparing_index=[i, index], sound=i)

    def SortingProcess(self):
        while(not self.Sorted()):
            self.Shuffle()
