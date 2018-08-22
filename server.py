#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import sleep
import random
import threading
from threading import Thread
import json

clients = {}
listeners = {}
terminate = False

class ClientThread(Thread):
    """docstring for ClientThread
        Commands for client:
        types: system, message
    """
    def __init__(self, name, conn, addr):
        super(ClientThread, self).__init__()
        self.name = name
        self.conn = conn
        self.addr = addr

    def run(self):
        """Launch thread"""
        ip, port = self.addr
        print('[client:{}:{}]'.format(str(ip), str(port)), 'is started.')

        while not terminate:
            data = self.conn.recv(1024)

            if data.decode() in dir(self):
                func = getattr(self, data.decode())
                func()
            elif data:
                response = self.response('message', data.decode())
                print(response)
                for idx in clients:
                    if (port not in clients[idx]['address']):
                        clients[idx]['connect'].send(response)
            else: 
                break

            sleep(1)

    def response(self, command, data):
        ip, port = self.addr
        response = {
            'client': '{}:{}'.format(str(ip), str(port)),
            'command': command,
            'data': data
        }

        return json.dumps(response).encode()

    def online(self):
        data = self.response('system', 'Current online: ' + str(len(clients)))
        self.conn.send(data)


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
                    print('[client:{}:{}]'.format(ip, port), 'is terminated.')
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
        ip, port = addr
        client_id = 'client-{}-{}-{}'.format(client_number, ip, port)
        clients[client_id] = {
            'thread': ClientThread(client_id, conn, addr),
            'connect': conn,
            'address': addr
        }
        clients[client_id]['thread'].setDaemon(True)
        clients[client_id]['thread'].start()

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
    
        