import sys
import math as m
#from scipy.optimize import fsolve
def cos(x): return m.cos(m.radians(x))
def tan(x): return m.tan(m.radians(x))
def sin(x): return m.sin(m.radians(x))
def acos(x): return m.degrees(m.acos(x))
def asin(x): return m.degrees(m.asin(x))
def atan(x): return m.degrees(m.atan(x))
def sqrt(x): return m.sqrt(x)
def frac(x,y): return(x/y)
def fpow(x,y,z): return((x/y)**z)
def c(x,y): return m.comb(x,y)
pi = m.pi
gc = 6.67e-11
ge = 9.81
ms = 1.989e30
yr = 365*24*3600
au = 1.496e11
ea = 23.5
def equations(variables):
    unknown1, unknown2 = variables
    #eq1 =
    #eq2 =
    return [eq1, eq2]
#fsolve(equations, [1,1])

x = 26**4-3*26**3+3*26**2-26
print(f"{x:e}")
