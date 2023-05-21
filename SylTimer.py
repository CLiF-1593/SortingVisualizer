import time


class SylTimer:
    def __init__(self):
        self.start = None
        self.passed = 0

    def clock(self, sec: float):
        if self.start is None:
            self.start = time.time()

        while time.time() - self.start - sec < self.passed:
            pass
        self.passed += sec

    def zero(self):
        self.passed = 0
        self.start = time.time()
