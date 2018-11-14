#！/usr/bin/evn python
# _*_ coding:utf-8 _*_

from time import sleep
from threading import current_thread, Thread, RLock

lock = RLock()

def show():
    with lock:
        print(current_thread().name, i)
        sleep(0.1)

def test():
    with lock:
        for i in range(3):
            show()

for i in range(2):
    Thread(target=test).start()

