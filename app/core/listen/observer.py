from app.core.traits.observer import ObserverTrait
import re
import json

class ListenObserver(ObserverTrait):
    """docstring for ListenObserver"""
    def parse_command(self, response):
        """parse response command"""
        # response = '{"data": "message text", "command": "test", "client": "192.168.0.1:16889"}'
        try:
            data = json.loads(response)
            if 'command' in data:
                command = data['command']
                self.observer.event(command, data)
            else:
                print('Command not found in response. ', response)    
        except:
            # if response format not defined
            print('Can\'t convert response to dictionary. ', response)