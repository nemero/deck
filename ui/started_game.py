import npyscreen
from widget_event_button import EventButton

class StartedGameForm(npyscreen.ActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Started Game:"
        self.OK_BUTTON_TEXT = "Restart"
        self.CANCEL_BUTTON_TEXT = "Exit"
        self.__class__.OK_BUTTON_BR_OFFSET = (2,6)
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 18)
        self.keypress_timeout = 10

        self.add_handlers({
            "1": self.when_choice_btn_take_card,
            "2": self.when_choice_btn_finish,
        })

        self.w_server_name = self.add(npyscreen.FixedText, 
                    name="Note:", 
                    value="Server: <host name>",
                    editable=False
                )

        self.nextrely += 2

        self.btn_take_card = self.add(EventButton, 
                    name="1. Take Card", 
                    callback=self.when_choice_btn_take_card
                )

        self.btn_finish = self.add(EventButton, 
                    name="2. Finish (2:00 mins)", 
                    callback=self.when_choice_btn_finish
                )

        self.nextrely -= 5

        self.w_players_grid = self.add(PlayerGameGridColTitles,
                    values=[
                        ['1. Player 1', 'Playing...'], 
                        ['2. Your Nick 2', 0],
                        ['3. Player 3', 'Waiting...'],
                        ['4. Player 4', 17],
                        ['5. Player 5', 21],
                        ['6. Player 6', 22],
                    ],
                    col_titles = [
                        'Score',
                        'A'
                    ],
                    select_whole_line=True,
                    scroll_exit=True,
                    max_height=7,
                    column_width=15,
                    relx=40,
                )

        self.w_server_name = self.add(npyscreen.FixedText, 
                    name="Note:", 
                    value="Your cards:",
                    editable=False,
                    relx=40
                )

    def when_choice_btn_take_card(self, widget):
        pass

    def when_choice_btn_finish(self, widget=None, *args, **keywords):
        self.parentApp.setNextForm("FinishedGame")
        self.editing = False

    def on_ok(self):
        # Prevent Next Form until the game is over
        self.editing = True
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")


class PlayerGameGridColTitles(npyscreen.GridColTitles):
    """docstring for SessionGridColTitles"""
    def custom_print_cell(self, actual_cell, cell_display_value):
        #row_idx, col_idx = actual_cell.grid_current_value_index

        #if isinstance(cell_display_value, int):
        if cell_display_value == 'Waiting...':
            actual_cell.color = 'LABEL'
        elif cell_display_value == 'Playing...':
            actual_cell.color = 'CAUTION'
        # elif col_idx == 2 and 15 > int(cell_display_value) < 21:
        #     actual_cell.color = 'CAUTION'
        # elif col_idx == 2 and int(cell_display_value) > 22:
        #     actual_cell.color = 'DANGER'
        # elif col_idx == 2 and int(cell_display_value) == 21:
        #     actual_cell.color = 'GOOD'
        else:
            actual_cell.color = 'DEFAULT'


        