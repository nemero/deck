import socket
from app.core.listen.thread import ListenThread
from time import sleep

class Connection:
    """docstring for Connection"""
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.is_terminate = False
        
    def connect(self, observer):
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.observer = observer
        self.observer.register('shutdown', 'after-shutdown')
    
        listen = ListenThread(name='listen', sock=self.sock, observer=self.observer)
        listen.setDaemon(True)
        listen.start()

    def run(self):
        while self.is_terminate == False:
            try:
                # If sock is closed and user enter any key it'll raise throw
                msg = input()
                self.sock.send(msg.encode())
            except:
                self.observer.event('after-shutdown', 'Client is terminated.')
                self.is_terminate = True

            sleep(1)

        self.observer.event('after-shutdown', 'Exit.')

    def send(self, data):
        sock.send(data.encode())

    def terminate(self, data):
        self.is_terminate = True
        self.sock.close()
        
    def finish(self, data=None):
        print(data)