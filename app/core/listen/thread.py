from threading import Thread
from app.core.listen.observer import ListenObserver
from time import sleep

class ListenThread(ListenObserver, Thread):
    """docstring for ListenThread"""
    def __init__(self, name, sock, observer, *args, **keywords):
        #print(ListenThread.mro())
        # it doesn't work..
        #super().__init__(*args, **keywords)

        ListenObserver.__init__(self, observer)
        Thread.__init__(self)
        
        self.name = name
        self.sock = sock

    def run(self):
        """Launch thread"""
        while True:
            try:
                # if sock is closed will raised throw
                data = self.sock.recv(1024)
                if data:
                    self.response(data)
                else:
                    break

            except:
                break

            sleep(1)

    def response(self, response):
    	# parse_command inherit from "interface"
    	self.parse_command(response.decode())