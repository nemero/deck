# not implemented

import npyscreen
from widget_event_button import EventButton

class VoteRestartGameForm(npyscreen.ActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Started Game:"
        self.OK_BUTTON_TEXT = "Restart (1)"
        self.CANCEL_BUTTON_TEXT = "Exit (2)"
        self.__class__.OK_BUTTON_BR_OFFSET = (2,6)
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 18)
        
        self.add_handlers({
            "1": self.on_ok,
            "2": self.on_cancel,
        })

        self.w_server_name = self.add(npyscreen.FixedText, 
                    name="Note:", 
                    value="Server: <host name>",
                    editable=False
                )

        self.w_players_grid = self.add(npyscreen.GridColTitles,
                    values=[
                        ['1. Player 1', 'Y'], 
                        ['2. Your Nick 2', ''],
                        ['3. Player 3', 'N'],
                        ['4. Player 4', ''],
                    ],
                    col_titles = [
                        'Player',
                        'Continue?'
                    ],
                    select_whole_line=True,
                    scroll_exit=True,
                    max_height=7,
                    column_width=15,
                    relx=40,
                )

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        # next form depending by your choice.
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")
        