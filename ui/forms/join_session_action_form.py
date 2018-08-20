import npyscreen
import curses
import weakref


class JoinSessionActionForm(npyscreen.ActionForm):
    """docstring for JoinSessionActionForm"""
    CREATE_SESSION_BUTTON_BR_OFFSET = (2, 30)
    OK_BUTTON_BR_OFFSET = (2,6)
    CANCEL_BUTTON_BR_OFFSET = (2, 18)
    CREATE_SESSION_BUTTON_TEXT = "Create Session"
    OK_BUTTON_TEXT = "Join"
    CANCEL_BUTTON_TEXT = "Back"

    def edit(self):
        # Add ok and cancel buttons. Will remove later
        tmp_rely, tmp_relx = self.nextrely, self.nextrelx

        cs_button_text = self.CREATE_SESSION_BUTTON_TEXT
        cmy, cmx = self.curses_pad.getmaxyx()
        cmy -= self.__class__.CREATE_SESSION_BUTTON_BR_OFFSET[0]
        cmx -= len(cs_button_text)+self.__class__.CREATE_SESSION_BUTTON_BR_OFFSET[1]
        self.cs_button = self.add_widget(self.__class__.OKBUTTON_TYPE, name=cs_button_text, rely=cmy, relx=cmx, use_max_space=True)
        cs_button_postion = len(self._widgets__)-1
        self.cs_button.update()
        
        c_button_text = self.CANCEL_BUTTON_TEXT
        cmy, cmx = self.curses_pad.getmaxyx()
        cmy -= self.__class__.CANCEL_BUTTON_BR_OFFSET[0]
        cmx -= len(c_button_text)+self.__class__.CANCEL_BUTTON_BR_OFFSET[1]
        self.c_button = self.add_widget(self.__class__.OKBUTTON_TYPE, name=c_button_text, rely=cmy, relx=cmx, use_max_space=True)
        c_button_postion = len(self._widgets__)-1
        self.c_button.update()
        
        my, mx = self.curses_pad.getmaxyx()
        ok_button_text = self.OK_BUTTON_TEXT
        my -= self.__class__.OK_BUTTON_BR_OFFSET[0]
        mx -= len(ok_button_text)+self.__class__.OK_BUTTON_BR_OFFSET[1]
        self.ok_button = self.add_widget(self.__class__.OKBUTTON_TYPE, name=ok_button_text, rely=my, relx=mx, use_max_space=True)
        ok_button_postion = len(self._widgets__)-1
        # End add buttons
        
        self.editing=True
        if self.editw < 0: self.editw=0
        if self.editw > len(self._widgets__)-1:
            self.editw = len(self._widgets__)-1
        if not self.preserve_selected_widget:
            self.editw = 0
    
    
        if not self._widgets__[self.editw].editable: self.find_next_editable()
        self.ok_button.update()

        self.display()

        while not self._widgets__[self.editw].editable:
            self.editw += 1
            if self.editw > len(self._widgets__)-2: 
                self.editing = False
                return False
        
        self.edit_return_value = None
        while self.editing:
            if not self.ALL_SHOWN: self.on_screen()
            try:
                self.while_editing(weakref.proxy(self._widgets__[self.editw]))
            except TypeError:
                self.while_editing()
            self._widgets__[self.editw].edit()
            self._widgets__[self.editw].display()
            
            self.handle_exiting_widgets(self._widgets__[self.editw].how_exited)
            
            if self.editw > len(self._widgets__)-1: self.editw = len(self._widgets__)-1
            if self.ok_button.value or self.c_button.value or self.cs_button.value:
                self.editing = False
        
            if self.ok_button.value:
                self.ok_button.value = False
                self.edit_return_value = self.on_ok()
            elif self.c_button.value:
                self.c_button.value = False
                self.edit_return_value = self.on_cancel()
            elif self.cs_button.value:
                self.cs_button.value = False
                self.edit_return_value = self.on_create_session()
        
        self.ok_button.destroy()
        self.c_button.destroy()
        self.cs_button.destroy()
        del self._widgets__[ok_button_postion]
        del self.ok_button
        del self._widgets__[c_button_postion]
        del self.c_button
        del self._widgets__[cs_button_postion]
        del self.cs_button
        self.nextrely, self.nextrelx = tmp_rely, tmp_relx
        self.display()
        self.editing = False
        
        return self.edit_return_value

    def on_create_session(self):
        pass
    