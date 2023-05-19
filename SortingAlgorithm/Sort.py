import time
from abc import abstractmethod
from enum import Enum
import threading
import random
from pysine import sine

class ArrayType(Enum):
    RANDOM = 0
    SORTED = 1
    REVERSED = 2

class Sort:
    class State(Enum):
        NOT_INITIALIZED = -1
        RESTING = 0
        SORTING = 1
        CHECKING = 2

    arr : list
    pivot : int
    comparing : list
    partition : list
    check : int
    delay : int
    thread : threading.Thread
    state : State
    playsound : bool

    #Pulbic Methods
    def __init__(self):
        self.InitValues()
        self.arr = []
        self.delay = 0
        self.thread = threading.Thread()
        self.state = Sort.State.NOT_INITIALIZED
        self.playsound = False

    def SetArray(self, arr: list):
        self.arr = arr
        self.state = Sort.State.RESTING

    def SetArray(self, size: int, type: ArrayType):
        self.arr = list(range(size))
        if type == ArrayType.REVERSED:
            self.arr.reverse()
        elif type == ArrayType.RANDOM:
            random.shuffle(self.arr)
        self.state = Sort.State.RESTING

    def SetSpeed(self, delay):
        self.delay = delay

    def SetPlaysound(self, playsound):
        self.playsound = playsound

    def Sort(self):
        if self.state == Sort.State.RESTING:
            self.state = Sort.State.SORTING
            self.thread = threading.Thread(target = self.SortingProcess)
            self.thread.start()

    def IsFinished(self):
        self.CheckState()
        return self.state == Sort.State.RESTING or self.state == Sort.State.NOT_INITIALIZED

    # Get Current Pivot (Integer Index, -1 : None)
    def GetPivot(self):
        return self.pivot

    # Get Comparing Index (Integer Index List, [] : None)
    def GetComparingIndex(self):
        return self.comparing

    # Get Partition (Integer Index List [begin, end], [] : None)
    def GetPartition(self):
        return self.partition

    # Get Last Checked Index (Integer Index, -1 : None)
    def GetCheckedIndex(self):
        return self.check

    #Private Methods
    @abstractmethod
    def SortingProcess(self): pass

    def Step(self, pivot : int = -1, comparing_index : list = [], partition : list = [], checked : int  = -1, sound : int = -1):
        self.pivot = pivot
        self.comparing = comparing_index
        self.partition = partition
        self.check = checked
        if self.playsound and sound != -1:
            if sound == len(self.arr):
                sound -= 1
            sine(frequency=400 + (1500 * self.arr[sound] // len(self.arr)), duration = self.delay)
        elif self.playsound and self.check != -1:
                sine(frequency=400 + (1500 * self.arr[self.check] // len(self.arr)), duration=self.delay * 2)
        else:
            time.sleep(self.delay)

    def CheckState(self):
        if self.state == Sort.State.SORTING and not self.thread.isAlive():
            self.state = Sort.State.CHECKING
            self.CheckArray()
        if self.state == Sort.State.CHECKING and not self.thread.isAlive():
            self.state = Sort.State.RESTING

    def CheckArray(self):
        self.InitValues()
        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                raise Exception("Sorting Failed!!!")
            self.Step(checked = i)
        self.Step(checked = len(self.arr) - 1)

    def InitValues(self):
        self.pivot = -1
        self.comparing = []
        self.partition = []
        self.check = -1