class Dialog(Frame):
    def __init__(self):
        Frame.__init__(self, master)
        self.list = Listbox(self, selectmode=EXTENDED)
        self.list.pack(fill=BOTH, expand=1)
        self.current = None
        self.poll()

        def poll(self):
            now = self.list.curselection()
            if now != self.current:
                self.list_has changed(now)
                self.current = now
            self.after(250, self.poll)

            def list_has_changed(self, selection):
                print "selction is", selection