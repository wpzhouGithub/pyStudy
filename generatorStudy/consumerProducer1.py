#!/usr/bin/evn python
# _*_ coding:utf-8 _*_

import time

def consumer():
    r = ''
    n = ''
    print('consumer in')
    while True:
        print('consumer true')
        print(n, 'before')
        n = yield r
        print(n, 'after')

        if not n:
            return

        print('consumer %s...'%n)

        time.sleep(4)
        r = '200 ok'

def produce(c):
    print('c in produce:', c)
    # c.next()
    n = 0;
    while n < 5:
        print('p producing %s...'%n)
        if n == 0:
            print(c.send(None))
        else:
            try:
                print(c.send('send:%s' % i))
            except Exception as e:
                print('e:', e)
        n += 1
    c.close()

if __name__ == '__main__':
    print('main in')
    c = consumer()
    produce(c)


