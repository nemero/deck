import npyscreen

class MainUI(npyscreen.NPSAppManaged):
    """docstring for MainUI"""
    def onStart(self):
        self.registerForm("MAIN", MainForm())
        self.registerForm("CreateServer", CreateServerForm())
     

class MainForm(npyscreen.Form):
    """docstring for MainForm"""
    def create(self):
        self.name = "Welcome to the Deck21!"

        self.nextrely += 5
        # Actions
        self.btn1 = self.add(npyscreen.Button, name="1. Create Session")
        self.btn2 = self.add(npyscreen.Button, name="2. Join to Session")
        self.btn3 = self.add(npyscreen.Button, name="3. Exit (Escape)")

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

    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")

    def while_editing(self, widget):
        #pass
        self.status_bar.value = "Note: {} has {}".format(widget.name, widget.value)

    def on_ok(self):
        # Prevent Next Form
        self.editing = True

    def on_cancel(self):
        print('form exit')
        exit()


class CreateServerForm(npyscreen.Form):
    """docstring for MainForm"""
    def create(self):
        self.name = "Create Server:"
        self.myName = self.add(npyscreen.TitleText, name="Name")
        self.maxPlayers = self.add(npyscreen.TitleText, name="Max Players")

    def afterEditing(self):
        self.parentApp.setNextForm(None)


class EventButton(npyscreen.Button):
    """docstring for EventButton"""
    def whenToggled(self):
        pass
        


if __name__ == '__main__':
    ui = MainUI().run()