import pickle

class user_vars:
    def __init__(self):
        self.Kultur                 = ""
        self.Schadbefall            = ""
        self.Wetter                 = ""
        self.Bodenbeschaffenheit    = ""

    def update_kultur(self, kultur):
        self.Kultur = kultur

    def update_schadbefall(self, schadbefall):
        self.Schadbefall = schadbefall

    def update_bodenbeschaffenheit(self, bodenbeschaffenheit):
        self.Bodenbeschaffenheit = bodenbeschaffenheit

    def update_wetter(self, wetter ):
        self.Wetter = wetter


