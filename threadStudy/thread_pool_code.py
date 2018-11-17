# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
import time
import threading
from random import random
from Queue import Queue


def double(n):
    return n * 2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        print('run in')
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print 'USE: %s' % self.name  # 线程名字
                print f(*args, **kwargs)
            except Exception as e:
                print e
            self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=2):
        self._q = Queue(num_t)
        # Create Worker Thread
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()


print 'create thread pool start!!!'
pool = ThreadPool()
print 'create thread pool end!!!'
time.sleep(10)
for _ in range(4):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)
pool.wait_complete()