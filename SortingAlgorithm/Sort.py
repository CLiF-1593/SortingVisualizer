from enum import Enum
import random

class ArrayType(Enum):
    RANDOM = 0
    SORTED = 1
    REVERSED = 2

class Sort:
    arr : list

    def __init__(self):
        self.arr = []

    def SetArray(self, arr: list):
        self.arr = arr

    def SetArray(self, size: int, type: ArrayType):
        self.arr = range(size)
        if type == ArrayType.REVERSED:
            self.arr.reverse()
        elif type == ArrayType.RANDOM:
            random.shuffle(self.arr)

    def Sort(self):
        