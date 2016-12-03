from tkinter import *

# class searchOptions:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Tk.frame(self.master)
#         kulturOptions = [
#             "Hafer",
#             "Roggen",
#             "Kartoffeln"
#         ]
#         kultur = StringVar(queryWindow)
#         kultur.set(kulturOptions[0])
#         kulturDropdown = OptionMenu(queryWindow, kultur, *kulturOptions)
#         kulturLabel = Label(master=queryWindow, text="Kultur")
#
#         self.kulturCheckbox.pack(side="left")
#         self.kulturDropdown.pack(side="right")


def manageCropClick():
    ##### Open ManageCropWindow #####
    print("lol")

def queryClick():
    ##### Open QueryWindow #####
    queryWindow = Toplevel()
    queryWindow.title("Query")
    queryWindow.geometry("300x200")

    ####### Select Search options ##########
    kulturOptions = [
        "Hafer",
        "Roggen",
        "Kartoffeln"
    ]
    kultur = StringVar(queryWindow)
    kultur.set(kulturOptions[0])
    kulturDropdown = OptionMenu(queryWindow, kultur, *kulturOptions)
    kulturLabel = Label(master=queryWindow, text="Kultur")

    befallOptions = [
        "Stängelbrand",
        "Milben"
    ]
    befall = StringVar(queryWindow)
    # befall.set(befallOptions[0])
    befall.set("-")
    befallDropdown = OptionMenu(queryWindow, befall, *befallOptions)
    befallDropdown.configure(state=DISABLED)
    befallCheckbox = Checkbutton(master=queryWindow, text="Befall",
                                 command=lambda: checkedBefall(befallDropdown, kultur))


    # searchOpts = searchOptions(master=queryWindow)
    querySearchButton = Button(master=queryWindow, text="Search", command=searchQueryClick)

    ##### arrangements #####
    kulturLabel.grid(row=0, column=1)
    kulturDropdown.grid(row=0, column=3)
    befallCheckbox.grid(row=1, column=1)
    befallDropdown.grid(row=1, column=3)
    querySearchButton.grid(row=5, column=2)
    # kulturDropdown.pack(side=RIGHT)
    # kulturLabel.pack(side=LEFT)
    # befallCheckbox.pack(side=LEFT)
    # querySearchButton.pack(side=BOTTOM)


def checkedBefall(field, kultur):
    # get possible Befall
    swapActive(field)
    print()

def swapActive(field):
    field.configure(state="disabled") if field["state"] == NORMAL else field.configure(state="normal")

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

