import npyscreen
import curses

class JoinSessionForm(npyscreen.Form):
    """docstring for MainForm"""
    def create(self):
        self.name = "Join to Session:"

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        