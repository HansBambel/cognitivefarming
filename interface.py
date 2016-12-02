import pickle

class user_vars:
    def __init__(self):
        self.Kultur                 = ""
        self.Schadbefall            = ""
        self.Wetter                 = ""
        self.Bodenbeschaffenheit    = ""

    def update_kultur(self, kultur):
        self.Kultur = kultur
        self.save()

    def update_schadbefall(self, schadbefall):
        self.Schadbefall = schadbefall
        self.save()

    def update_bodenbeschaffenheit(self, bodenbeschaffenheit):
        self.Bodenbeschaffenheit = bodenbeschaffenheit
        self.save()

    def update_wetter(self, wetter):
        self.Wetter = wetter
        self.save()

    def new_user(self):
        self.update_kultur(input("Welche Kultur wird angebaut? "))
        self.update_schadbefall(input("Um welchen Schadbefall handelt es sich? "))
        self.update_wetter(input("Welches Wetter herrscht gerade? "))
        self.update_bodenbeschaffenheit(input("Was für eine Bodenbeschaffenheit herrscht? "))

    def print_all(self):
        print(self.Kultur, " ", self.Schadbefall, " ", self.Wetter, " ", self.Bodenbeschaffenheit)

    def load(self):
        with open("user_vars.p", "rb") as l:
            self.Kultur, self.Schadbefall, self.Wetter, self.Bodenbeschaffenheit = pickle.load(l)

    def save(self):
        with open("user_vars.p", "wb") as p:
            pickle.dump([self.Kultur, self.Schadbefall, self.Wetter, self.Bodenbeschaffenheit], p)



user = user_vars()

user_in = input("Hallo Farmboy, willst du Daten (L)aden, (A)nlegen, (U)pdaten? ")
if user_in == "L" or user_in == "l":
    user.load()
    print("Geladen:")
    user.print_all()
elif user_in == "A" or user_in == "a":
    user.new_user()
    user.print_all()
elif user_in == "U" or user_in == "u":
    print("Was hat sich geändert?")
    differ = input("(K)ultur, (S)chadbefall, (W)etter, (B)odenbeschaffung")
    if differ == "k" or user_in == "K":
        user.update_kultur(input("neue Kultur: "))
    elif differ == "s" or user_in == "S":
        user.update_schadbefall(input("neue Schadbefall: "))
    elif differ == "w" or user_in == "W":
        user.update_wetter(input("neues Wetter: "))
    elif differ == "b" or user_in == "B":
        user.update_bodenbeschaffenheit(input("neue Bodenbeschaffenheit: "))
else:
    print("Bye")