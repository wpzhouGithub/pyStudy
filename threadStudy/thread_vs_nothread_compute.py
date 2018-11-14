# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
import time
import threading


def profile(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end   = time.time()
        msg = '%s cost: %s' % (func, end-start)
        print(msg)
    return wrapper


def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2)


@profile
def nothread():
    fib(35)
    fib(35)


@profile
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

time.sleep(20)
nothread()
hasthread()