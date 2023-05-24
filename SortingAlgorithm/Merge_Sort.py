# =================================================================
# [GPL 2.0 License]
# Copyright (C) 2023 CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

from SortingAlgorithm.Sort import Sort

class MergeSort(Sort):
    def Merge(self, front, middle, back):
        buf = []
        p1 = front
        p2 = middle + 1
        self.Step(comparing_index=[p1, p2], partition=[front, back], sound=p1)
        while p1 <= middle and p2 <= back:
            if self.arr[p1] > self.arr[p2]:
                buf.append(self.arr[p2])
                self.Step(comparing_index=[p1, p2], partition=[front, back], sound=p2)
                p2 += 1
            else:
                buf.append(self.arr[p1])
                self.Step(comparing_index=[p1, p2], partition=[front, back], sound=p1)
                p1 += 1
        while p1 <= middle:
            buf.append(self.arr[p1])
            self.Step(comparing_index=[p1, p2], partition=[front, back], sound=p1)
            p1 += 1
        while p2 <= back:
            buf.append(self.arr[p2])
            self.Step(comparing_index=[p1, p2], partition=[front, back], sound=p2)
            p2 += 1
        for i in range(len(buf)):
            self.arr[i + front] = buf[i]
            self.Step(comparing_index=[i + front], partition=[front, back], sound = i + front)

    def SortingProcess(self, begin = 0, end = None):
        if end == None: end = len(self.arr) - 1
        self.Step(comparing_index = [begin, end], sound = begin, partition=[begin, end])
        if begin == end: return
        mid = (begin + end) // 2
        self.Step(pivot=mid, sound=mid, partition=[begin, end])
        self.SortingProcess(begin, mid)
        self.SortingProcess(mid + 1, end)
        self.Merge(begin, mid, end)