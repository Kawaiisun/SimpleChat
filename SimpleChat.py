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
        label.pack(fill="x", side="top", padx=10, pady=(10,0))

        label = Label(self, text="an open source peer to peer chat app")
        label["font"] = ("Helvetica", 12)
        label["fg"] = "#cccccc"
        label["bg"] = self["bg"]
        label["anchor"] = "w"
        label["padx"] = 10
        label.pack(fill="x", side="top", ipadx=10)

        frame = Frame(self, bg="#173f5f", height=450)
        frame.pack(fill="x", side="top", anchor="n", padx=10, pady=(15,0))
        frame.pack_propagate(0)

        label = Label(frame, text="bot: welcome!")
        label["font"] = ("Helvetica", 12)
        label["fg"] = "#f6d55c"
        label["bg"] = frame["bg"]
        label["anchor"] = "w"
        label["padx"] = 10
        label.pack(fill="x", side="top", ipadx=10, ipady=10)

        frame = Frame(self, bg="#173f5f", height=45)
        frame.pack(fill="x", side="top", anchor="n", padx=10, pady=(10,0))
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=0, minsize=43)
        #frame.pack_propagate(0)

        self.input = StringVar()
        entry = Entry(frame, textvariable=self.input, relief=FLAT)
        entry["font"] = ("Helvetica", 12)
        entry["fg"] = "#3caea3"
        entry["bg"] = frame["bg"]
        entry.grid(column=0, row=0, sticky=W+E+N+S, padx=10, pady=10)
        #entry.pack(fill="x", side="top", padx=10, pady=10)
        self.input.set("enter a message here...")

        button = Button(frame, relief=FLAT, bg="white")
        button.grid(column=1, row=0, sticky=W+E+N+S, padx=5, pady=5)


    def startApp (self):

        self.parent.mainloop()

#===============================================================================================

def main ():

    root = Tk()
    app = SimpleChatApp(root)
    app.startApp()

#===============================================================================================

main()
