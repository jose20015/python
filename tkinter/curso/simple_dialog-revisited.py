import tkSimpleDialog

class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        Label(master, text="Frist:").grid(row=0)
        Label(master, text="Second:").grid(row=1)

        self.e1 = entry(master)
        self.e2 = entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1#initial focus
    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())
        print first, second #or something


root = Tk()

d = MyDialog(root)
print d.result