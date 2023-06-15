from reaction import *
from data import *
from start import *
from moredata import *


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

    @staticmethod
    def moredata(num):
        md = Moredata(Initiation, num)


Initiation.run()
