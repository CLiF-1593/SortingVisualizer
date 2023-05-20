from SortingAlgorithm.Sort import Sort

class CountingSort(Sort):
    def SortingProcess(self):
        buf = [0] * (self.max_data+1)
        for i in range(len(self.arr)):
            buf[self.arr[i]] += 1
            self.Step(comparing_index = [i], sound = i)
        index = 0
        for i in range(len(buf)):
            while buf[i]:
                self.arr[index] = i
                self.Step(comparing_index=[index], sound=index)
                buf[i] -= 1
                index += 1