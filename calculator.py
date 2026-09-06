import sys
import math as m
from mpmath import findroot
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
def xcl(x): return m.factorial(x)
def sum(x,y,z): return ((y-x)//z+1)*(x+y)/2
pi = m.pi
gc = 6.67e-11
ge = 9.81
ms = 1.989e30
yr = 365*24*3600
au = 1.496e11
ea = 23.5
mn = 1.675e-27
me = 9.109e-31
qe = 1.602e-19
pc = 3.086e16
au = 1.496e11
hc = 70e3/1e6/pc
def equations(x):
	return (
	x**3-3*x**2+7*x-13)
# findroot(equations(x))
def factors(num):
    factors = []
    for indice in range(2,int(sqrt(num))+1):
        if num%indice==0:
            factors.append(indice)
            factors.append(num//indice)
    return factors

x=frac(3*0.25*hc**2, 8*pi*gc*me*1e-5)

print(f"{x:e}")
