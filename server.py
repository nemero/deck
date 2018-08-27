from server2.client_thread import ClientThread
from server2.monitor_thread import MonitorThread
from server2.listener import Listener

listener = {}
clients = {}

if __name__ == "__main__":
    try:
        monitor = MonitorThread('monitor-1')
        monitor.clients = clients
        #monitor.setDaemon(True)
        monitor.start()

        listener = Listener()
        listener.clients = clients
        listener.run()
    except:
        #print(e.strerror)
        print('Server Terminating...')
        monitor.terminate = True # stopping monitor thread
        listener.terminate() # stopping listener thread
