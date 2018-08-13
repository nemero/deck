#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread
from time import sleep

host = 'localhost'
identifier = ''
terminate = False

sock = socket.socket()
sock.connect((host, 8080))
nickname = input('Enter your nickname: \n')
sock.send(nickname.encode())

class ListenThread(Thread):
    """docstring for ListenThread"""
    def __init__(self, name):
        super(ListenThread, self).__init__()
        self.name = name

    def run(self):
        """Launch thread"""
        while terminate == False:
            data = sock.recv(1024)
            if data:
                print(data.decode())
            else:
                break

            sleep(1)

listen = ListenThread('listen')
listen.setDaemon(True)
listen.start()

while terminate == False:
    try:
        msg = input()
        sock.send(msg.encode())
    except:
        print('Client Terminated.')
        terminate = True

    sleep(1)

sock.close()