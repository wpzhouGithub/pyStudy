# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
import time
import threading
from random import random
from Queue import Queue

q = Queue()


def double(n):
    return n * 2


def producer():
    for _ in range(2):
        wt = random()
        time.sleep(wt)
        print('producer double')
        q.put((double, wt))


def consumer():
    while 1:
        print('consumer waiting')
        task, arg = q.get()
        print('consumer', arg, task(arg))
        q.task_done()


for target in(producer, consumer):
    t = threading.Thread(target=target)
    t.start()