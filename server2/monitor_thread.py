from time import sleep
from threading import Thread

class MonitorThread(Thread):
    """docstring for MonitorThread"""
    def __init__(self, name):
        super(MonitorThread, self).__init__()
        self.name = name
        self.terminate = False
        self.clients = {}

    def run(self):
        """Launch thread"""
        while not self.terminate:
            index_del = []
            for idx in self.clients:
                #print(client.is_alive(), client.ident)
                if self.clients[idx]['thread'].is_alive() == False and self.clients[idx]['thread'].ident != None:
                    ip, port = self.clients[idx]['address']
                    print('[client:{}:{}]'.format(ip, port), 'is terminated.')
                    index_del.append(idx)

            # Remove terminated threads from client list
            if len(index_del):
                # need lock theards until we clear peers
                for idx in index_del:
                    del self.clients[idx]

            sleep(5)

        print('[Server]: Monitor is stopped.')

