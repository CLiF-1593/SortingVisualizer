from SortingAlgorithm.Sort import Sort

class BubbleSort(Sort):
    def SortingProcess(self):
        for i in range(len(self.arr) - 1, 1, -1):
            change = False
            for j in range(i):
                self.Step(comparing_index=[j])
                self.Step(comparing_index=[j + 1])
                if self.arr[j] > self.arr[j + 1]:
                    self.Step(comparing_index=[j, j + 1])
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    change = True
                    self.Step(comparing_index = [j, j+1])
            if not change:
                break