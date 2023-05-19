from SortingAlgorithm.Sort import Sort
import heapq

class HeapSort(Sort):
    def SortingProcess(self):
        heap = self.arr.copy()
        heapq.heapify(heap)
        for i in range(len(heap)):
            self.arr[i] = heap[i]
            self.Step(comparing_index=i, sound = i)
        for i in range(len(heap)):
            self.arr[i] = heapq.heappop(heap)
            self.Step(comparing_index=i, sound = i)