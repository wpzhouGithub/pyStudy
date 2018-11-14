#！/usr/bin/evn python
# _*_ coding:utf-8 _*_

from threading import  Event, Thread
import  time

def test_event():
    e = Event()
    def test():
        for i in range(5):
            print('start wait')
            print(1, e.isSet())
            time.sleep(4)
            e.set()
            print(4, e.isSet())
            e.wait()
            print(2, e.isSet())
            e.clear()
            print(3, e.isSet())

            print(i)

    Thread(target=test).start()
    return e

e = test_event()
print('e:',e)
