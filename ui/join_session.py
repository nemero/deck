import npyscreen
import curses
from forms.join_session_action_form import JoinSessionActionForm

class JoinSessionForm(JoinSessionActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Join to Session:"
        
        session_list = self.add(SessionGridColTitles, 
            name="Select exist session",
            select_whole_line=True,

            )
        session_list.col_titles = [
            'Server Name',
            'Status'
        ]
        session_list.values = [
            ['Host name 1', 'Live'], 
            ['Host name 2'],
            ['Host name 3', 'Protected'],
            ['Host name 4', 'Full'],
        ]

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("JoinSessionWaiting")

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")

    def on_create_session(self):
        self.parentApp.setNextForm("CreateSession")
        

class SessionGridColTitles(npyscreen.GridColTitles):
    """docstring for SessionGridColTitles"""
    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'Live':
            actual_cell.color = 'GOOD'
        elif cell_display_value == 'Full':
            actual_cell.color = 'DANGER'
        else:
            actual_cell.color = 'DEFAULT'
        