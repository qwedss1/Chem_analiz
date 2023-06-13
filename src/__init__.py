from reaction import *
from data import *
from start import *

class Initiation:
    def __init__(self):
        self.p = None
        self.s = None
        self.d = None
        self.menu()

    def cleanup(self, untouch):
        if self.s and untouch != self.s:
            del self.s
        if self.p and untouch != self.p:
            del self.s
        if self.d and untouch != self.d:
            del self.s

    def menu(self):
        self.s=start(self)
        self.cleanup(self.s)

    def reaction(self):
        self.p = Reaction(self)
        self.cleanup(self.p)

    def data(self):
        self.d = Data()
        self.cleanup(self.d)


i = Initiation()
