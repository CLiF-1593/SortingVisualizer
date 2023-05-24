# =================================================================
# [GPL 2.0 License]
# Copyright (C) 2023 CLiF and Syeosle
# See https://github.com/CLiF-1593/SortingVisualizer/blob/master/LICENSE for more details.
# =================================================================

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


if __name__ == '__main__':
    delay = 0.0000005
    t_len = 60
    repeat = int(t_len / delay)

    e_flag = False

    print(f'delay = {delay * 1000} ms\ntest length = {t_len} sec\ntotal calls = {repeat}')

    s = SylTimer()
    print('\nstart clock')
    for _ in range(5):
        s.zero()
        t = time.time()
        for _ in range(repeat):
            if time.time() - t > 2 * t_len:
                print('ERROR IS LONGER THAN TIME LENGTH')
                e_flag = True
                break
            s.clock(delay)

        du = time.time() - t
        if not e_flag: print(f'E(ms) = {round((du - t_len) * 1000, 3)}')
        e_flag = False

    #

    '''print('\nstart sleep')
    for _ in range(5):
        t = time.time()
        for _ in range(repeat):
            if time.time() - t > 2 * t_len:
                print('ERROR IS LONGER THAN TIME LENGTH')
                e_flag = True
                break
            time.sleep(delay)

        du = time.time() - t
        if not e_flag: print(f'E(ms) = {round((du - t_len) * 1000, 3)}')
        e_flag = False'''
