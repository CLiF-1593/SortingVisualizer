# Copyright (C) 2023 CLiF and Syeosle
#
# [MIT License]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
