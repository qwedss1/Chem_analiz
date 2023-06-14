import sqlite3 as sq
import json
import sympy as sp
import math
import chempy as cp
import os


class solve:
    def __init__(self, number):
        self.number = number
        a = "Reactions/Reaction"+str(number)+"/React.json"
        with open(a, "r") as file:
            self.reac = json.load(file)
        self.reag = self.reac["R"]
        self.prod = self.reac["P"]
        self.temp = self.reac["T"]
        self.dH = 0
        self.dG = 0
        self.reaction, self.coefs = self.balance(self.reag, self.prod)

        for n in range(0,len(self.reag)):
            conn = sq.connect('db.db')
            cur = conn.cursor()
            a = f"SELECT dH FROM therdb WHERE formula='{self.reag[n][0]}'"
            cur.execute(a)
            l = cur.fetchone()
            self.dH -= self.coefs[0][n]*(self.H(self.reag[n][0],self.temp)+float(l[0]))
        for n in range(0,len(self.prod)):
            conn = sq.connect('db.db')
            cur = conn.cursor()
            a = f"SELECT dH FROM therdb WHERE formula='{self.prod[n][0]}'"
            cur.execute(a)
            l = cur.fetchone()
            self.dH += self.coefs[1][n]*(self.H(self.prod[n][0],self.temp)+float(l[0]))
        for n in range(0,len(self.reag)):
            self.dG -= self.coefs[0][n]*self.G(self.reag[n][0],self.temp)
        for n in range(0,len(self.prod)):
            self.dG += self.coefs[1][n]*self.G(self.prod[n][0],self.temp)
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
            a = f"SELECT t{n} FROM therdb WHERE formula='{formula}'"
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
    def G(self,formula,t):
        T = []
        conn = sq.connect('db.db')
        cur = conn.cursor()
        a = f"SELECT Tmax FROM therdb WHERE formula='{formula}'"
        cur.execute(a)
        b = int(cur.fetchone()[0])
        a = f"SELECT ndG FROM therdb WHERE formula='{formula}'"
        cur.execute(a)
        c = int(cur.fetchone()[0])
        if c != 0:
            for n in range(1, c + 1):
                a = f"SELECT TA{n} FROM therdb WHERE formula='{formula}'"
                cur.execute(a)
                l = cur.fetchone()[0]
                T.append(l)
                if l > t:
                    break
            n = len(T)
            a = f"SELECT AA{n},BA{n},CA{n},DA{n},EA{n},FA{n},GA{n} FROM therdb WHERE formula='{formula}'"
            cur.execute(a)
            b =cur.fetchone()
            GT = self.dGT(b,t)
        else:
            GT=0
        return GT

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
        dirtreag, dirtprod = cp.balance_stoichiometry(onlyreag, onlyprod)
        reaction = ""
        for n in range(0, len(reag)):
            if n != len(reag) - 1:
                if dirtreag[f"{reag[n][0]}"] != 1:
                    reaction = reaction + str(dirtreag[f"{reag[n][0]}"]) + f"{reag[n][0]}"+" + "
                else:
                    reaction = reaction + f"{reag[n][0]}"+" + "
            else:
                if dirtreag[f"{reag[n][0]}"] != 1:
                    reaction = reaction + str(dirtreag[f"{reag[n][0]}"]) + f"{reag[n][0]}"
                else:
                    reaction = reaction + f"{reag[n][0]}"
        reaction = reaction + " = "
        for n in range(0, len(prod)):
            if n != len(prod)-1:
                if dirtprod[f"{prod[n][0]}"] != 1:
                    reaction = reaction + str(dirtprod[f"{prod[n][0]}"]) + f"{prod[n][0]}"+" + "
                else:
                    reaction = reaction + f"{prod[n][0]}"+" + "
            else:
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
        a = {"Reaction":f"{self.reaction}","dH":str(self.dH),"dG":str(self.dG),"dS":str(self.dS)}
        b = "Reactions/Reaction" + str(self.number)+ "/Calcu.json"
        with open(b, "w") as f:
            json.dump(a, f)
