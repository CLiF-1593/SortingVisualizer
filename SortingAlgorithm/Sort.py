import time
from abc import abstractmethod
from enum import Enum
import threading
import random

class ArrayType(Enum):
    RANDOM = 0
    SORTED = 1
    REVERSED = 2

class Sort:
    arr : list
    pivot : int
    comparing : list
    partition : list
    finish : bool
    delay : int

    #Pulbic Methods
    def __init__(self):
        self.arr = []
        self.finish = False

    def SetArray(self, arr: list):
        self.arr = arr

    def SetArray(self, size: int, type: ArrayType):
        self.arr = list(range(size))
        if type == ArrayType.REVERSED:
            self.arr.reverse()
        elif type == ArrayType.RANDOM:
            random.shuffle(self.arr)

    def SetSpeed(self, delay):
        self.delay = delay

    def Sort(self):
        sorting = threading.Thread(target = self.SortingProcess)
        sorting.start()

    def GetPivot(self):
        return self.pivot

    def GetComparingIndex(self):
        return self.comparing

    def GetPartition(self):
        return self.partition

    #Private Methods
    @abstractmethod
    def SortingProcess(self): pass

    def Step(self, pivot : int, comparing_index : list, partition : list):
        self.pivot = pivot
        self.comparing = comparing_index
        self.partition = partition
        time.sleep(self.delay)