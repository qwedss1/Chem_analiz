import math
from sympy import Symbol,Eq, solve,plot
from solve import solve as solvechem
class ms:
    R=8.31
    @staticmethod
    def engac(A,k,T):
        Ea = (math.log(A)-math.log(k))*(ms.R*T)
        return Ea
    @staticmethod
    def Kravn(num):
        A = solvechem(num)
        Kr = math.exp(-A.dG/(ms.R*A.temp))
        return Kr
    @staticmethod
    def EqMolLStech(num):
        A = solvechem(num)
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
        b = ms.returnz(solve(eqn,z)[0],A)
        return b
    @staticmethod
    def EqMolGStech(num,P):
        A = solvechem(num)
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
        eq = Eq(c*(P*(1-z)*(all+ca*z))**ca,ms.Kravn(num))
        b = ms.returnz(solve(eq, z)[0], A)
        return b
    @staticmethod
    def returnz(z,A):
        a = [z,[]]
        for n in range(0, len(A.reag)):
            a[1].append((A.reag[n][0],A.coefs[0][n]-z))
        for n in range(0, len(A.prod)):
            a[1].append((A.prod[n][0],A.coefs[0][n]+z))
        return a

    @staticmethod
    def graphik(A,num):
        ch= solvechem(num)
        x = Symbol('x')
        eq = math.log(A) - ch.dG/(ms.R*x)
        plot(eq,(x,298,500))

