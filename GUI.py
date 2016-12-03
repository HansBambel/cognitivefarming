from tkinter import *
import retrieval

class searchOptions:
    def __init__(self, master):
        self.master = master
        # self.frame = Tk.frame(self.master)
        ####### Select Search options ##########
        self.kultur = StringVar(master)
        self.kultur.set("Futterrübe")
        self.kulturOptions = retrieval.retrieveCultures()  # get Cultures from Database
        self.kulturDropdown = OptionMenu(master, self.kultur, *self.kulturOptions, command=self.updateBefall)
        self.kulturLabel = Label(master=master, text="Kultur")

        self.befall = StringVar(master)
        self.befall.set("")
        self.befallDropdown = OptionMenu(master, self.befall, [])
        self.befallDropdown.configure(state=DISABLED)
        self.checkvar = IntVar()
        self.befallCheckbox = Checkbutton(master=master, text="Befall", variable=self.checkvar,
                                     command=lambda: self.checkedBefall())

        self.kulturLabel.grid(row=0, column=1)
        self.kulturDropdown.grid(row=0, column=3)
        self.befallCheckbox.grid(row=1, column=1)
        self.befallDropdown.grid(row=1, column=3)

    def checkedBefall(self):
        # get possible Befall
        if self.checkvar.get():         # if checked
            befallListe = retrieval.retrieveBefall(self.kultur.get())
            self.befallDropdown['menu'].delete(0, 'end')
            for choice in befallListe:
                self.befallDropdown["menu"].add_command(label=choice, command=lambda v=choice: self.befall.set(v))
            self.befall.set(self.befallDropdown["menu"].entrycget(0, "label"))
            self.setActive(self.befallDropdown)
        else:                           # unchecked
            self.befall.set("")
            self.setInactive(self.befallDropdown)

    def setActive(self, field):
        field.configure(state="normal")

    def setInactive(self, field):
        field.configure(state="disable")

    def updateBefall(self, val):
        if self.checkvar.get():     # if befall is checked
            befallListe = retrieval.retrieveBefall(val)
            self.befallDropdown['menu'].delete(0, 'end')
            for choice in befallListe:
                self.befallDropdown["menu"].add_command(label=choice, command=lambda v=choice: self.befall.set(v))
            self.befall.set(self.befallDropdown["menu"].entrycget(0, "label"))

def manageCropClick():
    ##### Open ManageCropWindow #####
    print("lol")

def queryClick():
    ##### Open QueryWindow #####
    queryWindow = Toplevel()
    queryWindow.title("Query")
    queryWindow.geometry("500x200")


    searchOpts = searchOptions(master=queryWindow)
    querySearchButton = Button(master=queryWindow, text="Search", command=searchQueryClick)

    ##### arrangements #####
    # kulturLabel.grid(row=0, column=1)
    # kulturDropdown.grid(row=0, column=3)
    # befallCheckbox.grid(row=1, column=1)
    # befallDropdown.grid(row=1, column=3)
    # searchOpts.grid(row=0, column=0)
    querySearchButton.grid(row=5, column=2)



def searchQueryClick():
    print("searching")


mainWindow = Tk()
mainWindow.configure(background="black")
mainWindow.title("Crop Planner")
mainWindow.geometry("400x240")

manageCropButton = Button(master=mainWindow, text="Manage Crop", command=manageCropClick)
queryButton = Button(master=mainWindow, text="Get Info about regulations", command=queryClick)


# manageCropButton.grid(row=0, rowspan=2,columnspan=4, sticky=N)
# queryButton.grid(row=3, rowspan=2, sticky=N)
manageCropButton.pack(fill=BOTH, padx=10, pady=10)
queryButton.pack(fill=BOTH, padx=10, pady=10)


mainWindow.mainloop()

