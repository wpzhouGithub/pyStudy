# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self, n=10):
        def fib(n):
            if n <= 2:
                return 1
            return fib(n - 1) + fib(n - 2)
        return fib(n)

if __name__ == '__main__':
    start = time.time()
    for i in range(3):
        p = MyProcess(str(i))
        p.start()
    for i in range(3):
        p.join()

    print('cost: ', time.time() - start)