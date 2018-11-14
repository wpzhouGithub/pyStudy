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


def read_file():
    file_name = '/mnt/data/blockchain/data/steem_data//21860001-21870000.txt'
    with open(file_name, 'r') as f:
        lines = f.readlines()
        print(len(lines))


@profile
def nothread():
    read_file()
    read_file()


@profile
def hasthread():
    for i in range(2):
        t = threading.Thread(target=read_file, args=())
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

nothread()
hasthread()