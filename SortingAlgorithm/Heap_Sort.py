from Sort import Sort
import heapq

class HeapSort(Sort):
    def heapify(self,index, begin_point, end_point):
        largest = index
        self.Step(pivot = index, sound = index, partition = [begin_point, end_point])
        left_index = 2 * (index - begin_point) + 1 + begin_point
        right_index = 2 * (index - begin_point) + 2 + begin_point
        if left_index <= end_point and self.arr[left_index] > self.arr[largest]:
            largest = left_index
        if right_index <= end_point and self.arr[right_index] > self.arr[largest]:
            largest = right_index
        if largest != index:
            self.Step(comparing_index=[largest, index], sound=largest, partition=[begin_point, end_point])
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            self.Step(comparing_index=[largest, index], sound=largest, partition=[begin_point, end_point])
            self.heapify(largest, begin_point, end_point)

    def SortingProcess(self, begin = None, end = None):
        if begin == None:
            begin = 0
            end = len(self.arr) - 1
        for i in range(begin + (end - begin + 1) // 2 - 1, begin - 1, -1):
            self.heapify(i, begin, end)
        for i in range(end, begin, -1):
            self.Step(comparing_index=[0, i], sound = i, partition = [begin, i])
            self.arr[begin], self.arr[i] = self.arr[i], self.arr[begin]
            self.Step(comparing_index=[0, i], sound = i, partition=[begin, i])
            self.heapify(begin, begin, i - 1)