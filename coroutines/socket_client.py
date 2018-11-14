# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
import  socket

def run(n):
    sock = socket.socket()
    sock.connect(('localhost', 1234))
    sock.send('send: %s' % n)
    data = sock.recv(1024)
    print(str(n) + ' ' + data)

if __name__ == '__main__':
    for i in range(0, 3):
        run(i)
