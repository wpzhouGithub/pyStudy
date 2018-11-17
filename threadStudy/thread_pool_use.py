# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
from multiprocessing.pool import ThreadPool
import time

def worker():
    time.sleep(3)
    print('worker done!')

def fib(n=30):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)

w_start = time.time()
n_tread = 2
pool = ThreadPool(n_tread)
for _ in range(4):
    pool.apply_async(fib)

pool.close()
pool.join()
print('cost:', time.time() - w_start)

