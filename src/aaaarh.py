import sqlite3 as sq
import json
import sympy as sp
import math
import chempy as cp
import os


class solve:
    def __init__(self, number):
        self.number = number
        a = "Reactions/Reaction"+str(number)+"React.json"
        with open(a, "r") as file:
            self.reac = json.load(file)
        self.reag = self.reac.value("R")
        self.prod = self.reac.value("P")
        self.temp = self.reac.value("T")
        self.dH = 0
        self.dG = 0
        self.reaction, self.coefs = self.balance(self.reag, self.prod)

        for n in range(0,len(self.reag)):
            self.dH = self.dH - self.coefs[0][n]*self.H(self.reag[n],self.temp)
        for n in range(0,len(self.prod)):
            self.dH = self.dH + self.coefs[1][n]*self.H(self.prod[n],self.temp)
        for n in range(0,len(self.reag)):
            self.dG = self.dG - self.coefs[0][n]*self.G(self.reag[n],self.temp)
        for n in range(0,len(self.prod)):
            self.dG = self.dG + self.coefs[1][n]*self.G(self.prod[n],self.temp)
        self.dS = (self.dH-self.dG)/self.temp
        self.Calcu()
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
    def balance(self, reag, prod):
        onlyreag = []
        for n in range(0, len(reag)):
            onlyreag.append(reag[n][0])
        onlyprod = []
        for n in range(0, len(prod)):
            onlyprod.append(prod[n][0])
        print(onlyreag, onlyprod)
        dirtreag, dirtprod = cp.balance_stoichiometry(onlyreag, onlyprod)
        print(dirtreag, dirtprod)
        reaction = ""
        for n in range(0, len(reag)):
            if dirtreag[f"{reag[n][0]}"] != 1:
                reaction = reaction + str(dirtreag[f"{reag[n][0]}"]) + f"{reag[n][0]}"
            else:
                reaction = reaction + f"{reag[n][0]}"
        for n in range(0, len(prod)):
            if dirtprod[f"{prod[n][0]}"] != 1:
                reaction = reaction + str(dirtprod[f"{prod[n][0]}"]) + f"{prod[n][0]}"
            else:
                reaction = reaction + f"{prod[n][0]}"
        cre = []
        for n in range(0, len(reag)):
            cre.append(dirtreag[f"{reag[n][0]}"])
        cpr = []
        for n in range(0, len(reag)):
            cpr.append(dirtprod[f"{prod[n][0]}"])
        coefs = [cre, cpr]
        return reaction, coefs
    def Calcu(self):
        a = {"Reaction":f"{self.reaction}","dH":self.dH,"dG":self.dG,"dS":self.dS}
        b = "Reactions/Reaction" + self.number
        os.mkdir(b)
        b += "/" + "Calcu.json"
        with open(b, "a") as f:
            json.dump(self.a, f)