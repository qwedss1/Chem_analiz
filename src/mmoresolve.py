import math
from sympy import Symbol,Eq
import solve
class ms:
    R=8.31
    @staticmethod
    def engac(A,k,T):
        Ea = (math.log(A)-math.log(k))/(ms.R*T)
        return Ea
    @staticmethod
    def Kravn(Gt,T):
        Kr = math.exp(-Gt/(ms.R*T))
        return Kr
    @staticmethod
    def EqMolLStech(num):
        A = solve(num)
        z = Symbol('z')
        c = 1
        ca = 0
        for n in range(0,len(A.reag)):
            c = c / (A.coefs[0][n]**A.coefs[0][n])
        for n in range(0,len(A.prod)):
            c = c * (A.coefs[1][n]**A.coefs[1][n])
        for n in range(0, len(A.reag)):
            ca = ca - A.coefs[0][n]
        for n in range(0, len(A.prod)):
            ca = ca + A.coefs[1][n]
        eqn = Eq(c*(1-z)**ca,ms.Kravn(A.dG,A.temp))
    @staticmethod
    def EqMolGStech(num,P):
        A = solve(num)
        all = 0
        z = Symbol('z')
        for n in range(0, len(A.reag)):
            all = all + A.coefs[0][n]
        for n in range(0, len(A.prod)):
            all = all + A.coefs[1][n]
        c = 1
        ca = 0
        for n in range(0, len(A.reag)):
            c = c / (A.coefs[0][n] ** A.coefs[0][n])
        for n in range(0, len(A.prod)):
            c = c * (A.coefs[1][n] ** A.coefs[1][n])
        for n in range(0, len(A.reag)):
            ca = ca - A.coefs[0][n]
        for n in range(0, len(A.prod)):
            ca = ca + A.coefs[1][n]
        eq = Eq(c*(P*(1-z)*(all+ca*z))**ca)

