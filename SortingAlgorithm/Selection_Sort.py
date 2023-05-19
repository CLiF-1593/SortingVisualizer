from SortingAlgorithm.Sort import Sort

class SelectionSort(Sort):
    def SortingProcess(self):
        for i in range(0, len(self.arr) - 1):
            min = self.arr[i]
            index = i
            self.Step(comparing_index=[index])
            for j in range(i + 1, len(self.arr)):
                self.Step(pivot = i, comparing_index = [j, index])
                if min > self.arr[j]:
                    min = self.arr[j]
                    index = j
                    self.Step(pivot=i, comparing_index=[index])
            self.arr[i], self.arr[index] = self.arr[index], self.arr[i]
            self.Step(comparing_index=[i, index])