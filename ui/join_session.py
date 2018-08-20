import npyscreen
import curses
from forms.join_session_action_form import JoinSessionActionForm

class JoinSessionForm(JoinSessionActionForm):
    """docstring for MainForm"""
    def create(self):
        self.name = "Join to Session:"
        
        self.add_handlers({
            "1": self.when_select_session,
        })

        self.session_list = self.add(SessionGridColTitles,
                values=[
                    ['Host name 1', 'Live'], 
                    ['Host name 2'],
                    ['Host name 3', 'Protected'],
                    ['Host name 4', 'Full'],
                ],
                col_titles = [
                    'Server Name',
                    'Status'
                ],
                scroll_exit=True,
                max_height=7,
                max_width=60
            )

        self.nextrely += 1

        self.status_bar = self.add(npyscreen.FixedText, name="Note:", value="YOHOHO", 
                rely = -5, 
                relx=3,
                editable=False
            )

    def on_ok(self):
        # Prevent Next Form
        #self.editing = True
        self.parentApp.setNextForm("JoinSessionWaiting")

    def on_cancel(self):
        self.parentApp.setNextForm("MAIN")

    def on_create_session(self):
        self.parentApp.setNextForm("CreateSession")

    def when_select_session(self, widget):
        self.status_bar.value = "selected session"
        

class SessionGridColTitles(npyscreen.GridColTitles):
    """docstring for SessionGridColTitles"""
    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'Live':
            actual_cell.color = 'GOOD'
        elif cell_display_value == 'Full':
            actual_cell.color = 'DANGER'
        else:
            actual_cell.color = 'DEFAULT'
        