import npyscreen

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Welcome to Deck21!!!")

class MainForm(npyscreen.ActionForm):
    """Constructor"""
    def create(self):
        self.add(npyscreen.TitleText, name="Welcome to!")
        self.title = self.add(npyscreen.TitleText, name="TitleText", value="Hello World!", relx=5)
        #self.add(npyscreen.TitleFilename, name="Filename:", rely=-5)

    def on_ok(self):
        """Event on click Ok"""
        self.parentApp.setNextForm(None)
    
    def on_cancel(self):
        """Event on click Cancel"""
        self.title.value = "Hello World!"

MyApp = App()
MyApp.run()