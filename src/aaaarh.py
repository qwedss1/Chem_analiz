import sqlite3 as sq
import json
import sympy as sp
import math
class solve:
    def __init__(self,number):
        a = "Reactions/Reaction"+str(number)+"React.json"
        with open(a,"r") as file:
            self.reac = json.load(file)
        self.reag = self.reac.value("R")
        self.prod = self.reac.value("P")
        self.temp = self.reac.value("T")
    def H (self,formula,t):
        conn = sq.connect('db.db')
        cur = conn.cursor()


    def dHT(self,coefs,t):
        T=t
        a = coefs[0]*T+coefs[1]*T*T+coefs[2]/T+coefs[3]*math.sqrt(T)+coefs[4]*T*T*T+coefs[5]
        return a
    def dGT(self,coefs,t):
        T=t
        a = coefs[0]*T*math.log(T)+coefs[1]*T+coefs[2]*T*T+coefs[3]/T+coefs[4]*math.sqrt(T)+coefs[5]*T*T*T+coefs[6]
        return a