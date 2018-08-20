class CreateSession(object):
    """docstring for CreateSession"""
    def __init__(self, arg):
        super(CreateSession, self).__init__()
        self.arg = arg
        # will observe answers from server
        # observer['receive'].append({'created': self.receive})
        # observer['joined_player'].append({'created': self.joined_players})

    def create(self):
        # send command to create session
        # create_session -p=5 -n="session name"
        # connect.send("create_session -p5 -n='session name'")
        # 
        pass

    def receive(self):
        """the method will called when server return answer message with system answer 'created'"""
        pass

    def joined_players(self):
        """the method will called when anyone joined into created session so server will return answer with list of joined players"""
        pass
        