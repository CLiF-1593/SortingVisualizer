from SortingAlgorithm.Sort import Sort

class InsertionSort(Sort):
    def SortingProcess(self):
        for i in range(1, len(self.arr)):
            self.Step(comparing_index=[i], sound=i)
            while i and self.arr[i - 1] > self.arr[i]:
                self.Step(comparing_index=[i - 1, i], sound=i-1)
                self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
                self.Step(comparing_index=[i - 1, i], sound=i-1)
                i -= 1