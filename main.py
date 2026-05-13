import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b  = [i for i in a[0]]
c = defaultdict(int)
d = []
for i in b:
    c[i]+=1
for i in c.values():
    d.append(i)

e = [int(i) for i in a[1].split()]
f = [int(i) for i in a[2].split()]
g = int(a[3])
h = 0
#if e[0]>d[0] and e[1]>d[1] and e[2]>d[2]:

m = min(e[0]//d[0], e[1]//d[1], e[2]//d[2])
p = max(e[0]//d[0], e[1]//d[1], e[2]//d[2])
q = True
for i in range(m+1,p+2):
    n = (i-m*d[0])*f[0] + (i-m*d[1])*f[1] + (i-m*d[2])*f[2]
    if n>g:
        h += i-1
        q = False
if q==False:
    print(h)
else:
    g -= n
    h += p+1
    r = e[0]*f[0] + e[1]*f[1] + e[2]*f[2]
    h += g // r
    print(h)

