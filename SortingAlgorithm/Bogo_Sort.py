import math
from random import randrange

from Sort import Sort

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
