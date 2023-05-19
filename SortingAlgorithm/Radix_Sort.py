from SortingAlgorithm.Sort import Sort

class RadixSort(Sort):
    def SortingProcess(self):
        digit = 1
        buf = [[] for i in range(10)]
        while len(buf[0]) != len(self.arr):
            buf = [[] for i in range(10)]
            for i in range(len(self.arr)):
                index = (self.arr[i] // digit) % 10
                buf[index].append(self.arr[i])
                self.Step(comparing_index=[i], sound = i)
            index = 0
            for i in range(10):
                for j in range(len(buf[i])):
                    self.arr[index] = buf[i][j]
                    self.Step(comparing_index=[index], sound=index)
                    index += 1
            digit *= 10