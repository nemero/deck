from app.core.traits.observer import ObserverTrait

class ListenObserver(ObserverTrait):
    """docstring for ListenObserver"""
    def parse_command(self, response):
        """parse response command"""
        # parse command
        # TODO: implement
        command = 'test'
        data = {'data': 'message text'}
        print(self.observer)
        self.observer.event(command, data)