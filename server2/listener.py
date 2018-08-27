import socket
from server2.client_thread import ClientThread

class Listener:
    """docstring for Listener"""
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 8080))
        self.sock.listen(1)
        self.clients = {}

    def run(self):
        conn, addr = self.sock.accept()

        client_number = len(self.clients) + 1
        ip, port = addr
        client_id = 'client-{}-{}-{}'.format(client_number, ip, port)
        self.clients[client_id] = {
            'thread': ClientThread(client_id, conn, addr),
            'connect': conn,
            'address': addr
        }
        self.clients[client_id]['thread'].clients = self.clients
        self.clients[client_id]['thread'].setDaemon(True)
        self.clients[client_id]['thread'].start()

        self.run()

    def terminate(self):
        for idx in self.clients:
            print('Client {} is terminating...'.format(idx))
            self.clients[idx]['thread'].terminate()
        #self.sock.close()
        