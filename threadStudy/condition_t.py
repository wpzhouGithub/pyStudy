# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
import time
import threading

lines = []

def read_file():
    file_name = '/mnt/data/blockchain/data/steem_data//21860001-21870000.txt'
    with open(file_name, 'r') as f:
        global lines
        lines = f.readlines()


def consumer(cond):
    t = threading.currentThread()
    time.sleep(2)
    with cond:
        cond.wait()  # wait()方法创建了一个名为waiter的锁，并且设置锁的状态为locked。这个waiter锁用于线程间的通讯
        print '{}: Resource is available to consumer'.format(t.name)
        print('len of lines: %s' % len(lines))


def producer(cond):
    t = threading.currentThread()
    time.sleep(2)
    with cond:
        print '{}: Making resource available'.format(t.name)
        read_file()
        cond.notifyAll()  # 释放waiter锁，唤醒消费者


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

time.sleep(15)
c1.start()
print('c1 start')
c2.start()
print('c3 start')
time.sleep(2)
p.start()
print('p start')
