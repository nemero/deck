import npyscreen

class EventButton(npyscreen.Button):
    """docstring for EventButton"""
    def __init__(self, screen, name='Button', cursor_color=None, callback=None, *args, **keywords):
        super(EventButton, self).__init__(screen, name, cursor_color, *args, **keywords)
        self.callback = callback

    def whenToggled(self):
        if self.callback:
            #print(self.name)
            self.callback(widget=self)