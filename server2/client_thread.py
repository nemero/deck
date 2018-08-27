from time import sleep
from threading import Thread
import json
import datetime

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
        self.is_terminate = False
        self.clients = {}

    def run(self):
        """Launch thread"""
        ip, port = self.addr
        print('[client:{}:{}]'.format(str(ip), str(port)), 'is started.')

        while not self.is_terminate:
            data = self.conn.recv(1024)

            if data.decode() in dir(self):
                func = getattr(self, data.decode())
                func()
            elif data:
                response = self.response('message', data.decode())
                print(response)
                for idx in self.clients:
                    if (port not in self.clients[idx]['address']):
                        self.clients[idx]['connect'].send(response)
            else: 
                break

            sleep(1)

        self.conn.close()

    def response(self, command, data):
        ip, port = self.addr
        response = {
            'client': '{}:{}'.format(str(ip), str(port)),
            'command': command,
            'data': data
        }

        return json.dumps(response).encode()

    def info(self):
        data = self.response('info', {
                        'online': 'Current online: ' + str(len(self.clients)),
                        'sessions': 1,
                        'version': 'alpha'
                    })
        self.conn.send(data)

    def terminate(self):
        data = self.response('shutdown', {
                        'message': 'Server is shutdown',
                        'date': str(datetime.datetime.now())
                    })
        self.conn.send(data)
        self.is_terminate = True      
