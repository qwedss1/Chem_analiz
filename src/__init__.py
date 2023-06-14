from reaction import *
from data import *
from start import *


class Initiation:
    @staticmethod
    def run():
        Initiation.menu()

    @staticmethod
    def menu():
        s = start(Initiation)

    @staticmethod
    def reaction():
        p = Reaction(Initiation)

    @staticmethod
    def data(num):
        d = Data(Initiation, num)


Initiation.run()
