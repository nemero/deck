import npyscreen
import curses
from forms.w_players_grid import WidgetPlayersGrid

class JoinSessionWaitingForm(npyscreen.ActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Joined in Session:"
        self.OK_BUTTON_TEXT = "Start"
        self.CANCEL_BUTTON_TEXT = "Leave"
        self.__class__.OK_BUTTON_BR_OFFSET = (2,6)
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 18)
        
        self.w_server_name = self.add(npyscreen.FixedText, 
                    name="Note:", 
                    value="Server: <host name>",
                    editable=False
                )

        self.nextrely -= 1

        self.w_players_grid = self.add(WidgetPlayersGrid,
                    relx=40,
                    max_height=7,
                    column_width=30,
                    values=[
                        ['1. Player 1'],
                        ['2. Your Nick'],
                        ['3. Player 3']
                    ]
                )

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("StartedGame")

    def on_cancel(self):
        self.parentApp.setNextForm("JoinSession")
        