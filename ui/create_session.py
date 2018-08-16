import npyscreen
import curses

class CreateSessionForm(npyscreen.Form):
    """docstring for MainForm"""
    def create(self):
        self.name = "Create Session:"
        self.myName = self.add(npyscreen.TitleText, name="Name")
        self.maxPlayers = self.add(npyscreen.TitleText, name="Max Players")

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        