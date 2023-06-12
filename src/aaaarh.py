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

    def H(self,formula,t):
        T = []
        conn = sq.connect('db.db')
        cur = conn.cursor()
        a = f"SELECT Tmax FROM therdb WHERE formula='{formula}'"
        cur.execute(a)
        b = int(cur.fetchone()[0])
        a = f"SELECT ndH FROM therdb WHERE formula='{formula}'"
        cur.execute(a)
        c = int(cur.fetchone()[0])
        for n in range(1, c + 1):
            a = f"SELECT t{n} FROM therdb WHERE formula='Ag'"
            cur.execute(a)
            l = cur.fetchone()[0]
            T.append(l)
            if l > t:
                break
        n = len(T)
        a = f"SELECT a{n},b{n},c{n},d{n},e{n},f{n} FROM therdb WHERE formula='{formula}'"
        cur.execute(a)
        HT = self.dHT(cur.fetchone(),t)
        return HT

    def dHT(self,coefs,t):
        T=t
        a = coefs[0]*T+coefs[1]*T*T+coefs[2]/T+coefs[3]*math.sqrt(T)+coefs[4]*T*T*T+coefs[5]
        return a
    def dGT(self,coefs,t):
        T=t
        a = coefs[0]*T*math.log(T)+coefs[1]*T+coefs[2]*T*T+coefs[3]/T+coefs[4]*math.sqrt(T)+coefs[5]*T*T*T+coefs[6]
        return a
