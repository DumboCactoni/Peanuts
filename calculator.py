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
def rad(x): return x*m.pi/180
def deg(x): return x*180/m.pi
pi = m.pi
gc = 6.67e-11
ms = 1.989e30
yr = 365*24*3600
au = 1.496e11
ea = 23.5
me = 9.109e-31
mn = 1.675e-27
qe = 1.602e-192
pc = 3.086e16
ls = 3.828e26
tb = 13.8e9*yr
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

a = 9.81*sin(10)-0.4*9.81*cos(10)
b = 0.4*9.81*cos(10)*1e-3*500**2
x=acos(frac(a**2,b))/500

print(f"{x:e}")
