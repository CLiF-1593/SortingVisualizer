import time
from abc import abstractmethod
from enum import Enum
import threading
import random
from pysine import sine
from SylTimer import SylTimer


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

    arr: list
    pivot: int
    comparing: list
    partition: list
    check: int
    delay: list
    thread: threading.Thread
    state: State
    playsound: bool
    max_data: int
    run: bool

    # Pulbic Methods
    def __init__(self, timer: SylTimer):
        self.InitValues()
        self.arr = []
        self.delay = [0]
        self.thread = threading.Thread()
        self.state = Sort.State.NOT_INITIALIZED
        self.playsound = False
        self.max_data = 0
        self.timer = timer
        self.run = False

    def SetArrayDirectly(self, arr: list):
        self.arr = arr
        self.state = Sort.State.RESTING
        self.max_data = max(arr)

    def SetArray(self, size: int, unit: int, type: ArrayType):
        self.arr = list(range(0, size, unit))
        if type == ArrayType.REVERSED:
            self.arr.reverse()
        elif type == ArrayType.RANDOM:
            random.shuffle(self.arr)
        self.state = Sort.State.RESTING
        self.max_data = size - 1

    def SetSpeed(self, delay):
        self.delay[0] = delay

    def SetPlaysound(self, playsound):
        self.playsound = playsound

    def Sort(self):
        if self.state == Sort.State.RESTING:
            self.state = Sort.State.SORTING
            self.run = True
            self.thread = threading.Thread(target=self.sort_and_check)
            self.thread.start()

    def sort_and_check(self):
        self.SortingProcess()
        self.CheckState()


    def IsFinished(self):
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

    # Private Methods
    @abstractmethod
    def SortingProcess(self):
        pass

    def Step(self, pivot: int = -1, comparing_index: list = [], partition: list = [], checked: int = -1,
             sound: int = -1):
        self.pivot = pivot
        self.comparing = comparing_index
        self.partition = partition
        self.check = checked
        if self.playsound and sound != -1:
            if sound == len(self.arr):
                sound -= 1
            sine(frequency=400 + (2000 * self.arr[sound] // self.max_data), duration=self.delay[0])
        elif self.playsound and self.check != -1:
            sine(frequency=400 + (2000 * self.arr[self.check] // self.max_data), duration=self.delay[0])
        else:
            self.timer.clock(self.delay[0])

    def CheckState(self):
        if self.state == Sort.State.SORTING:
            self.state = Sort.State.CHECKING
            self.CheckArray()
            self.state = Sort.State.RESTING

    def CheckArray(self):
        self.InitValues()
        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                raise Exception("Sorting Failed!!!")
            self.Step(checked=i)
        self.Step(checked=len(self.arr) - 1)

    def InitValues(self):
        self.pivot = -1
        self.comparing = []
        self.partition = []
        self.check = -1
