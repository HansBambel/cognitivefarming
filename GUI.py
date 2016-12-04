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
        self.kulturDropdown.grid(row=0, column=2)
        self.befallCheckbox.grid(row=1, column=1)
        self.befallDropdown.grid(row=1, column=2)

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




class queryWindow:
    def __init__(self):
        ##### Open QueryWindow #####
        self.queryWindow = Toplevel()
        self.queryWindow.configure(background="orange")
        self.queryWindow.focus()
        self.queryWindow.title("Anfrage")
        self.queryWindow.geometry("1200x600")

        self.querySearchButton = Button(master=self.queryWindow, text="Suchen", command=self.searchQueryClick)
        self.searchLabelFrame = LabelFrame(master=self.queryWindow, text="Suchergebnisse")
        self.resultLabel = Label(master=self.searchLabelFrame)
        self.searchResults = Listbox(master=self.searchLabelFrame)
        self.searchResults.bind("<Double-1>", lambda i: self.moreInfo(i))

        ##### arrangements #####
        self.mySearchOptions = searchOptions(master=self.queryWindow)
        self.querySearchButton.grid(row=5, column=2, sticky=N+S+E+W)
        self.searchLabelFrame.grid(row=6, column=2, sticky=N+S+E+W)

        ### in LabelFrame ###
        self.resultLabel.pack()
        self.searchResults.pack()

    def moreInfo(self, infoProduct):
        infoProduct = self.searchResults.selection_get()
        kultur = self.mySearchOptions.kultur.get()
        befall = self.mySearchOptions.befall.get()
        wirkstoff, wirkstoffgehalt, zulassungsende, gefahrenstoffverordnung, hinweise \
            = retrieval.retrieveProductInfo(infoProduct, kultur, befall)
        # TODO give to Judith's function
        #### Create ProductInfoFrame ####
        self.productInfoFrame = LabelFrame(master=self.queryWindow, text=infoProduct)
        self.wirkstoffLabel = Label(master=self.productInfoFrame, text="Wirkstoff: " + ", ".join(wirkstoff))
        self.wirkstoffGehaltLabel = Label(master=self.productInfoFrame, text="Wirkstoffgehalt: " + ", ".join(wirkstoffgehalt))
        self.zulassungsendeLabel = Label(master=self.productInfoFrame, text="Zulassungsende: " + ", ".join(zulassungsende))
        self.hinweiseLabel = Label(master=self.productInfoFrame, text="Hinweise: " + ", ".join(hinweise), wraplengt=200)

        self.gefahrenstoffVerordnungLabelFrame = LabelFrame(master=self.productInfoFrame, text="Gefahrenstoffverordnung")
        self.gefahrenbereichListbox = Listbox(master=self.gefahrenstoffVerordnungLabelFrame)
        self.gefahrenbereichListbox.delete(0, END)
        ### Liste alle gefahrenstoffberecihe auf ###
        for i, bereich in enumerate(gefahrenstoffverordnung):
            self.gefahrenbereichListbox.insert(i, bereich)
        self.gefahrenbereichListbox.pack()


        ### put in InfoFrame
        self.wirkstoffLabel.pack()
        self.wirkstoffGehaltLabel.pack()
        self.zulassungsendeLabel.pack()
        self.gefahrenstoffVerordnungLabelFrame.pack()
        self.hinweiseLabel.pack()

        ### put in queryWindow
        self.productInfoFrame.grid(row=6, column=3, sticky=N+S+E+W)

    def searchQueryClick(self):
        resLabel=("Suche nach Pflanzenschutzmitteln für folgende Kultur: " + self.mySearchOptions.kultur.get() +
              " mit folgenden Schadbefall: " + self.mySearchOptions.befall.get())
        self.resultLabel.configure(text=resLabel)

        results = retrieval.retrieveSchutzmittel(culture=self.mySearchOptions.kultur.get(),
                                             disease=self.mySearchOptions.befall.get())

        self.searchResults.delete(0, END)
        for i, result in enumerate(results):
            self.searchResults.insert(i, result)

        self.resultLabel.pack()
        self.searchResults.pack(fill=BOTH)


class manageCropWindow:
    def __init__(self):
        self.manageCropWindow = Toplevel()
        self.manageCropWindow.focus()
        self.manageCropWindow.title("Planung der Ernte")
        self.manageCropWindow.geometry("600x400")

def queryClick():
    ##### Open QueryWindow #####
    myQueryWindow = queryWindow()

def manageCropClick():
    ##### Open ManageCropWindow #####
    myManageCropWindow = manageCropWindow()


mainWindow = Tk()
mainWindow.configure(background="orange")
mainWindow.title("Amazone Helfer")
mainWindow.geometry("400x240")
logo = PhotoImage(file="amazone-touch-icon-144px.gif")
w1 = Label(mainWindow, image=logo).pack(side="bottom")

manageCropButton = Button(master=mainWindow, text="Ernte planen", command=manageCropClick)
queryButton = Button(master=mainWindow, text="Pflanzenschutzregularien prüfen", command=queryClick)


# manageCropButton.grid(row=0, rowspan=2,columnspan=4, sticky=N)
# queryButton.grid(row=3, rowspan=2, sticky=N)
manageCropButton.pack(fill=BOTH, padx=10, pady=10)
queryButton.pack(fill=BOTH, padx=10, pady=10)


mainWindow.mainloop()

