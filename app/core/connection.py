import socket
from app.core.listen.thread import ListenThread
from time import sleep

class Connection:
    """docstring for Connection"""
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.terminate = False
        
    def connect(self, observer):
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))

        listen = ListenThread(name='listen', sock=self.sock, observer=observer)
        listen.setDaemon(True)
        listen.start()

    def run(self):
        while self.terminate == False:
            try:
                msg = input()
                self.sock.send(msg.encode())
            except:
                print('Client Terminated.')
                self.terminate = True

            sleep(1)

        self.sock.close()

    def send(self, data):
        sock.send(data.encode())
        
        