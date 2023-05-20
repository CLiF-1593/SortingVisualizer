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