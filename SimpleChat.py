from tkinter import *

#===============================================================================================

#notes:
#   -Ctrl+Shift+B will RUN the PRGM (make sure you have "script" addon installed)
#   -Ctrl+/ will COMMENT a BLOCK

#===============================================================================================

class SimpleChatApp (Frame):

    def __init__ (self, parent):

        Frame.__init__(self, parent, bg="#20639b")
        self.parent = parent
        self.pack(expand=True, fill="both")
        self.makeWidgets()

    def makeWidgets (self):

        window = self.winfo_toplevel()
        window.title("SimpleChat")
        window.geometry("400x600")

        label = Label(self, text="SimpleChat")
        label["font"] = ("Helvetica", 18, "bold")
        label["fg"] = "white"
        label["bg"] = self["bg"]
        label["anchor"] = "w"
        label["padx"] = 10

        label.pack(fill="x", side="top", ipadx=10, ipady=10)

    def startApp (self):

        self.parent.mainloop()

#===============================================================================================

def main ():

    root = Tk()
    app = SimpleChatApp(root)
    app.startApp()

#===============================================================================================

main()
