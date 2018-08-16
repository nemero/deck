import npyscreen
import curses

class CreateSessionForm(npyscreen.ActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Create Session:"
        self.OK_BUTTON_TEXT = "Continue"
        self.CANCEL_BUTTON_TEXT = "Cancel"
        self.__class__.OK_BUTTON_BR_OFFSET = (2,6)
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 18)

        self.myName = self.add(npyscreen.TitleText, name="Enter host name:")
        self.maxPlayers = self.add(npyscreen.TitleText, name="Enter max players:")

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("CreateSessionWaiting")

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")
        