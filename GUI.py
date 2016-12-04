'''
@author: Kevin Trebing
@email: ktrebing@uos.de

'''

from tkinter import *
import retrieval
import textToSpeech
import retrieveRankFunction
import wetter_warnung

class searchOptions:
    def __init__(self, master):
        self.master = master
        ####### Select Search options ##########
        self.kultur = StringVar(master)
        self.kultur.set("Futterrübe")
        self.kulturOptions = retrieval.retrieveCultures()  # get Cultures from Database
        self.kulturDropdown = OptionMenu(master, self.kultur, *self.kulturOptions, command=self.updateBefall)
        self.kulturLabel = Label(master=master, text="Kultur", bg="orange")

        self.befall = StringVar(master)
        self.befall.set("")
        self.befallDropdown = OptionMenu(master, self.befall, [])
        self.befallDropdown.configure(state=DISABLED)
        self.checkvar = IntVar()
        self.befallCheckbox = Checkbutton(master=master, text="Befall", variable=self.checkvar,
                                     command=lambda: self.checkedBefall(), bg="orange")

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
        bgcolor = "orange"
        highlightcolor = "green"
        self.queryWindow = Toplevel()
        self.queryWindow.configure(background=bgcolor)
        self.queryWindow.focus()
        self.queryWindow.title("Anfrage")
        self.queryWindow.geometry("1400x600")

        self.querySearchButton = Button(master=self.queryWindow, text="Suchen", command=self.searchQueryClick)
        self.searchLabelFrame = LabelFrame(master=self.queryWindow, text="Suchergebnisse")
        self.resultLabel = Label(master=self.searchLabelFrame, wraplengt=200)
        self.searchResults = Listbox(master=self.searchLabelFrame)
        self.searchResults.bind("<Double-1>", lambda i: self.getProductInfo(i))
        self.weatherLabel = Label(master=self.queryWindow, text=wetter_warnung.wetter_check(), wraplengt=200, bg=bgcolor)

        ##### arrangements #####
        self.mySearchOptions = searchOptions(master=self.queryWindow)
        self.weatherLabel.grid(row=1, column=3, sticky=E+W)
        self.querySearchButton.grid(row=5, column=2, sticky=N+S+E+W)
        self.searchLabelFrame.grid(row=6, column=2, sticky=N+E+W)

        ### in LabelFrame ###
        self.resultLabel.pack()
        self.searchResults.pack()

    def getProductInfo(self, infoProduct):
        infoProduct = self.searchResults.selection_get()
        kultur = self.mySearchOptions.kultur.get()
        befall = self.mySearchOptions.befall.get()
        wirkstoff, wirkstoffgehalt, zulassungsende, self.gefahrenstoffverordnung, hinweise \
            = retrieval.retrieveProductInfo(infoProduct, kultur, befall)
        #### Create ProductInfoFrame ####
        self.productInfoFrame = LabelFrame(master=self.queryWindow, text=infoProduct)
        self.wirkstoffLabel = Label(master=self.productInfoFrame, text="Wirkstoff: " + ", ".join(wirkstoff))
        self.wirkstoffGehaltLabel = Label(master=self.productInfoFrame, text="Wirkstoffgehalt: " + ", ".join(wirkstoffgehalt))
        self.zulassungsendeLabel = Label(master=self.productInfoFrame, text="Zulassungsende: " + ", ".join(zulassungsende))
        self.hinweiseLabel = Label(master=self.productInfoFrame, text="Hinweise: " + ", ".join(hinweise), wraplengt=250)

        self.gefahrenstoffVerordnungLabelFrame = LabelFrame(master=self.productInfoFrame, text="Gefahrenstoffverordnung")
        self.gefahrenbereichListbox = Listbox(master=self.gefahrenstoffVerordnungLabelFrame)
        self.gefahrenbereichListbox.delete(0, END)
        ### Liste alle gefahrenstoffbereiche auf ###
        for i, bereich in enumerate(self.gefahrenstoffverordnung):
            self.gefahrenbereichListbox.insert(i, bereich)
        self.gefahrenbereichListbox.pack()
        self.gefahrenbereichListbox.bind("<Double-1>", lambda j: self.getBereichsinfo(j))


        ### put in InfoFrame
        self.wirkstoffLabel.pack()
        self.wirkstoffGehaltLabel.pack()
        self.zulassungsendeLabel.pack()
        self.gefahrenstoffVerordnungLabelFrame.pack()
        self.hinweiseLabel.pack()

        ### put in queryWindow
        self.productInfoFrame.grid(row=6, column=3, sticky=N+S+E+W)


    def getBereichsinfo(self, val):
        self.gefahrenbereichLabelFrame = LabelFrame(master=self.queryWindow, text="Gefahrenbereich")
        self.bereichListbox = Listbox(master=self.gefahrenbereichLabelFrame)
        self.bereichListbox.delete(0, END)
        tmp = self.gefahrenstoffverordnung[self.gefahrenbereichListbox.selection_get()]
        for k, area in enumerate(tmp[0].split(", ")):  # not a nice workaround
            self.bereichListbox.insert(k, area)
        self.bereichListbox.bind("<Double-1>", lambda l: self.getRegularie(l))

        self.bereichListbox.pack()
        # put in queryWindow
        self.gefahrenbereichLabelFrame.grid(row=6, column=4, sticky=N+S+E+W)

    def getRegularie(self, val):
        reg = self.bereichListbox.selection_get()
        regString = retrieveRankFunction.retrieveRankFunction(reg)
        # regString = "Philipp. Sprech doch mal endlich Hochdeutsch, du komischer Bayer. Am anderen Tisch gibt es viel bessere Hochdeutschsprechende Menschen."

        self.regFrame = LabelFrame(master=self.queryWindow, text=reg)
        self.regLabel = Label(master=self.regFrame, text=regString, wraplengt=250)
        self.speakButton = Button(master=self.regFrame, text="Vorlesen", command=lambda: self.readWatson(regString))

        self.regLabel.pack()
        self.speakButton.pack()

        self.regFrame.grid(row=6, column=5, sticky=N+W+E)

    def readWatson(self, stringToRead):
        textToSpeech.say_text(stringToRead)


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
        image = PhotoImage(file="pantera.gif")
        w1 = Label(self.manageCropWindow, image=image).pack()
        self.manageCropWindow.configure(bg="orange")
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

manageCropButton.pack(fill=BOTH, padx=10, pady=10)
queryButton.pack(fill=BOTH, padx=10, pady=10)

mainWindow.mainloop()

