#！/usr/bin/evn python
# _*_ coding:utf-8 _*_

from threading import Thread, Condition, current_thread
from time import  sleep, time
from random import  randint
from queue import  Queue

class MyThread(Thread):

    def __init__(self, func, args, name=""):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args
        self.res = ""

    def getResult(self):
        return self.res

    def run(self):
        print("starting", self.name, "at:", time())
        self.res = self.func(*self.args)
        print(self.name, "finished at:", time())


def writeQ(queue):
    print("producting object for Q... at:", time())
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def readQ(queue):
    print('readQ at:', time())
    queue.get(1)
    print("consumed object from Q... size now", queue.qsize(), " at:", time())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(8)

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(1)

funcs = [writer,  reader]
nfuncs = range(len(funcs))

def main():
    nloops = 6
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
        print("getResult:", thread.getResult())

    print("all Done")

if __name__ == "__main__":
    main()








