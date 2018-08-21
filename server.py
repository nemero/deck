#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import sleep
import random
import threading
from threading import Thread

clients = {}
listeners = {}
terminate = False

class ClientThread(Thread):
    """docstring for ClientThread
        Commands for client:
        online
        take - for get card
        finish = for finish game and waiting other players
    """
    player = None
    
    def __init__(self, name, conn, addr):
        super(ClientThread, self).__init__()
        self.name = name
        self.conn = conn
        self.addr = addr

    def base_str(self):
        ip, port = self.addr
        return '[Client]: ' + str(ip) + ' ' + str(port)

    def run(self):
        """Launch thread"""
        ip, port = self.addr
        print(self.base_str(), 'is started.')

        while not terminate:
            data = self.conn.recv(1024)

            if data.decode() in dir(self):
                func = getattr(self, data.decode())
                func()
            elif data:
                print(self.base_str(), 'message:', data.decode())
                msg = self.base_str() + ' message: ' + data.decode()
                for idx in clients:
                    if (port not in clients[idx]['address']):
                        clients[idx]['connect'].send(msg.encode())
            else: 
                break

            sleep(1)

    def online(self):
        data = 'Current online: ' + str(len(clients))
        self.conn.send(data.encode())


class MonitorThread(Thread):
    """docstring for MonitorThread"""
    def __init__(self, name):
        super(MonitorThread, self).__init__()
        self.name = name

    def run(self):
        """Launch thread"""
        while not terminate:
            index_del = []
            for idx in clients:
                #print(client.is_alive(), client.ident)
                if clients[idx]['thread'].is_alive() == False and clients[idx]['thread'].ident != None:
                    ip, port = clients[idx]['address']
                    print('[Client]:', ip, port, clients[idx]['thread'].name, 'is terminated.')
                    index_del.append(idx)

            # Remove terminated threads from client list
            if len(index_del):
                # need lock theards until we clear peers
                for idx in index_del:
                    del clients[idx]

            sleep(5)

        print('[Server]: Monitor is stopped.')


class Listener(object):
    """docstring for Listener"""
    sock = None

    def __init__(self):
        super(Listener, self).__init__()
        self.sock = socket.socket()
        self.sock.bind(('', 8080))
        self.sock.listen(1)

    def run(self):
        conn, addr = self.sock.accept()
        client_number = len(clients) + 1
        clients[client_number] = {
            'thread': ClientThread('client-' + str(client_number), conn, addr),
            'connect': conn,
            'address': addr
        }
        clients[client_number]['thread'].setDaemon(True)
        clients[client_number]['thread'].start()

        self.run()
        

if __name__ == "__main__":
    monitor = MonitorThread('monitor-1')
    #monitor.setDaemon(True)
    monitor.start()

    try:
        listener = Listener()
        listener.run()
    except Exception as e:
        print(e.strerror)
        listener.sock.close()
        terminate = True

    # listener = Listener()
    # listener.run()

    #listener.sock.close()
    # clients[0] = ClientThread('client-1')
    # clients[1] = ClientThread('client-2')

    # clients[0].setDaemon(True)
    # clients[0].start()

    # clients[1].setDaemon(True)
    # clients[1].start()
    
        