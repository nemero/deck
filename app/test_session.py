class TestSession(object):
    """docstring for TestSession"""
    def __init__(self):
        super(TestSession, self).__init__()
        # will observe answers from server
        # observer['receive'].append({'created': self.receive})
        # observer['joined_player'].append({'created': self.joined_players})

    def test(self, data):
        print(self)
        print(data)

    def test_v2(self, data):
        print('called test_v2 event')