from tkinter import *
import retrieval

class searchOptions:
    def __init__(self, master):
        self.master = master
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

    def getKultur(self):
        return self.kultur

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
    # TODO
    print("lol")

class queryWindow:
    def __init__(self):
        ##### Open QueryWindow #####
        self.queryWindow = Toplevel()
        self.queryWindow.title("Query")
        self.queryWindow.geometry("500x200")

        self.querySearchButton = Button(master=self.queryWindow, text="Search", command=self.searchQueryClick)

        ##### arrangements #####
        self.mySearchOptions = searchOptions(master=self.queryWindow)
        self.querySearchButton.grid(row=5, column=2)



    def searchQueryClick(self):
        print("searching in cultures: ", self.mySearchOptions.kultur.get(), " for the following pests: ",
              self.mySearchOptions.befall.get())
        print(retrieval.retrieveSchutzmittel(culture=self.mySearchOptions.kultur.get(),
                                             disease=self.mySearchOptions.befall.get()))


def queryClick():
    myQueryWindow = queryWindow()

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

