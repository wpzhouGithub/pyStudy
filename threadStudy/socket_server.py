# -*- coding: UTF-8 -*-
'''
Created on Aug 16, 2018

@author: wpzhou
'''
from multiprocessing.pool import ThreadPool
import socket

server = socket.socket()
server.bind(('', 12345))
server.listen(6)

print('--------等待客户端连接------')
def worker(conn):
    while True:
        recv_data = conn.recv(1024)
        if recv_data:
            print(recv_data)
            conn.send(recv_data)
        else:
            conn.close()
            break

if __name__ == '__main__':
    pool = ThreadPool(3)
    while True:
        conn, address = server.accept()
        pool.apply_async(worker, args=(conn,))