import sys
import math as m
from mpmath import findroot
from fractions import Fraction as fr
def cos(x): return m.cos(m.radians(x))
def tan(x): return m.tan(m.radians(x))
def sin(x): return m.sin(m.radians(x))
def acos(x): return m.degrees(m.acos(x))
def asin(x): return m.degrees(m.asin(x))
def atan(x): return m.degrees(m.atan(x))
def sqrt(x): return m.sqrt(abs(x))
def frac(x,y): return(x/y)
def fpow(x,y,z): return((x/y)**z)
def c(x,y): return m.comb(x,y)
def xcl(x): return m.factorial(x)
def sum(x,y,z): return ((y-x)//z+1)*(x+y)/2
def rad(x): return x*m.pi/180
def deg(x): return x*180/m.pi
pi = m.pi
gc = 6.67e-11
pk = 6.626e-34
ms = 1.989e30
rs = 6.96e8
re = 6378e3
Me = 5.972e24
sb = 5.67e-8
yr = 365*24*3600
au = 1.496e11
ec = 23.5
me = 9.109e-31
mn = 1.675e-27
qe = 1.602e-19
pc = 3.086e16
ls = 3.828e26
tb = 13.8e9*yr
am = 1.66e-27
pl = 6.626e-34
rd = 1.096e7
#def equations(x):
#	return (
#	a*x**(-3/2)+b*sqrt(x)-c)
# x = findroot(equations, [r,r*2], solver='anderson', maxsteps=1000, verify=False)
def factors(num):
    factors = []
    for indice in range(2,int(sqrt(num))+1):
        if num%indice==0:
            factors.append(indice)
            factors.append(num//indice)
    return factors
# fr(x).limit_denominator()


x = fpow(4*1.096e7*660e-9, 1.096e7*660e-9-4, 1/2)
print(f"{x:.3e}")