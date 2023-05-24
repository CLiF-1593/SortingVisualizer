# =================================================================
# [GPL 2.0 License]
# Copyright (C) 2023 CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

import time
from abc import abstractmethod
from enum import Enum
import random
from pysine import sine
from PyQt5.QtCore import QThread
from SylTimer import SylTimer


class ArrayType(Enum):
    RANDOM = 0
    SORTED = 1
    REVERSED = 2


class Thread(QThread):
    def __init__(self, target=None):
        super().__init__()
        self.target = target

    def run(self):
        if self.target:
            self.target()

class Sort:
    class State(Enum):
        NOT_INITIALIZED = -1
        RESTING = 0
        SORTING = 1
        CHECKING = 2

    arr: list
    pivot: list
    comparing: list
    partition: list
    check: list
    delay: list
    thread: Thread
    state: State
    playsound: list
    max_data: int
    run: bool

    # Pulbic Methods
    def __init__(self, timer: SylTimer):
        self.pivot = [-1]
        self.comparing = [[]]
        self.partition = [[]]
        self.check = [-1]
        self.arr = []
        self.delay = [0]
        self.thread = Thread()
        self.state = Sort.State.NOT_INITIALIZED
        self.playsound = [False]
        self.max_data = 0
        self.timer = timer
        self.run = False

    def Copy(self, target):
        self.arr = target.arr
        self.delay = target.delay
        self.playsound = target.playsound
        self.pivot = target.pivot
        self.comparing = target.comparing
        self.partition = target.partition
        self.check = target.check
        self.max_data = target.max_data

    def SetArrayDirectly(self, arr: list):
        self.arr = arr.copy()
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
        if not playsound:
            self.timer.zero()
        self.playsound[0] = playsound

    def Sort(self):
        if self.state == Sort.State.RESTING:
            self.state = Sort.State.SORTING
            self.run = True
            self.thread = Thread(target=self.sort_and_check)
            self.thread.start()

    def sort_and_check(self):
        self.SortingProcess()
        tmp = self.delay[0]
        self.delay[0] = 0.5 / len(self.arr)
        self.CheckState()
        self.delay[0] = tmp
        del tmp


    def IsFinished(self):
        return self.state == Sort.State.RESTING or self.state == Sort.State.NOT_INITIALIZED

    # Get Current Pivot (Integer Index, -1 : None)
    def GetPivot(self):
        return self.pivot[0]

    # Get Comparing Index (Integer Index List, [] : None)
    def GetComparingIndex(self):
        return self.comparing[0]

    # Get Partition (Integer Index List [begin, end], [] : None)
    def GetPartition(self):
        return self.partition[0]

    # Get Last Checked Index (Integer Index, -1 : None)
    def GetCheckedIndex(self):
        return self.check[0]

    def Stop(self):
        if self.thread.isRunning():
            self.thread.terminate()

    # Private Methods
    @abstractmethod
    def SortingProcess(self):
        pass

    def Step(self, pivot: int = -1, comparing_index: list = [], partition: list = [], checked: int = -1,
             sound: int = -1):
        self.pivot[0] = pivot
        self.comparing[0] = comparing_index
        self.partition[0] = partition
        self.check[0] = checked
        if self.playsound[0] and sound != -1:
            if sound == len(self.arr):
                sound -= 1
            sine(frequency=500 + (2000 * self.arr[sound] // (self.max_data + 1)), duration=self.delay[0])
        elif self.playsound[0] and self.check[0] != -1:
            sine(frequency=500 + (2000 * self.arr[self.check[0]] // (self.max_data + 1)), duration=self.delay[0])
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
        self.pivot[0] = -1
        self.comparing[0] = []
        self.partition[0] = []
        self.check[0] = -1