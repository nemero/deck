import npyscreen
from widget_event_button import EventButton
from join_session import JoinSessionForm
from create_session import CreateSessionForm

class MainUI(npyscreen.NPSAppManaged):
    """docstring for MainUI"""
    def onStart(self):
        self.registerForm("MAIN", MainForm())
        self.registerForm("CreateSession", CreateSessionForm())
        self.registerForm("JoinSession", JoinSessionForm())
     

class MainForm(npyscreen.Form):
    """docstring for MainForm"""
    def create(self):
        self.name = "Welcome to the Deck21!"
        self.keypress_timeout = 10

        self.add_handlers({
            "1": self.when_choice_btn1,
            "2": self.when_choice_btn2,
            "3": self.exit_application,
        })

        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application

        self.nextrely += 5
        # Actions
        self.btn1 = self.add(EventButton, name="1. Create Session", callback=self.when_choice_btn1)
        self.btn2 = self.add(EventButton, name="2. Join to Session", callback=self.when_choice_btn2)
        self.btn3 = self.add(EventButton, name="3. Exit (Escape)")

        self.online = self.add(npyscreen.FixedText, name="none", value="Online: 5", 
                                        rely=7, 
                                        relx=28,
                                        editable=False
                                        )

        self.online = self.add(npyscreen.FixedText, name="none", value="Sessions: 1", 
                                        rely=8, 
                                        relx=28,
                                        editable=False
                                        )

        self.status_bar = self.add(npyscreen.FixedText, name="Note:", value="YOHOHO", 
                                        rely = -5, 
                                        relx=3,
                                        editable=False
                                        )

    # TODO: add handlers on number hotkeys 1, 2, 3 and Escape
    def when_choice_btn1(self, widget=None, *args, **keywords):
        #self.status_bar.value = "Note: {} has {}".format('btn', widget)
        #self.display()
        self.parentApp.setNextForm("CreateSession")
        self.editing = False

    def when_choice_btn2(self, widget=None, *args, **keywords):
        #self.status_bar.value = "Note: {} has {}".format('btn', widget)
        #self.display()
        self.parentApp.setNextForm("JoinSession")
        self.editing = False

    def exit_application(self, *args, **keywords):
        self.parentApp.setNextForm(None)
        self.editing = False

    def on_ok(self):
        # Prevent Next Form
        self.editing = True

    def on_cancel(self):
        print('form exit')
        exit()

    

if __name__ == '__main__':
    ui = MainUI().run()