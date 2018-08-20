import npyscreen

class FinishedGameForm(npyscreen.ActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Finish Game:"
        self.OK_BUTTON_TEXT = "Restart (0:17 min)"
        self.CANCEL_BUTTON_TEXT = "Exit"
        self.__class__.OK_BUTTON_BR_OFFSET = (2,6)
        self.__class__.CANCEL_BUTTON_BR_OFFSET = (2, 28)
        
        self.w_server_name = self.add(npyscreen.FixedText,
                    value="Server: <host name>",
                    editable=False
                )

        self.nextrely += 1
        
        self.w_players_grid = self.add(PlayerFinishGridColTitles,
                    values=[
                        ['1. Player 1', 'Playing...'], 
                        ['2. Your Nick 2', 17],
                        ['3. Player 3', 22],
                        ['4. Player 4', 21],
                    ],
                    col_titles = [
                        'Score',
                        'A'
                    ],
                    select_whole_line=True,
                    scroll_exit=True,
                    max_height=7,
                )


    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("StartedGame")

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")
        

class PlayerFinishGridColTitles(npyscreen.GridColTitles):
    """docstring for SessionGridColTitles"""
    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'Playing...':
            actual_cell.color = 'DEFAULT'
        elif cell_display_value == '21':
            actual_cell.color = 'GOOD'
        else:
            actual_cell.color = 'DEFAULT'