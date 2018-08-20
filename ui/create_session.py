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

        self.host_name = self.add(npyscreen.TitleText, name="Enter host name:", begin_entry_at=30)
        self.max_players = self.add(npyscreen.TitleText, name="Enter max players:", begin_entry_at=30)

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("CreateSessionWaiting")

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")
        