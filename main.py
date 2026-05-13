import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b  = [i for i in a[0]]
c = defaultdict(int)
for i in b:
    c[i]+=1
t = ["B","S","C"]
d = [c[i] if i in c else 10**-9 for i in t]

e = [int(i) for i in a[1].split()]
f = [int(i) for i in a[2].split()]
g = int(a[3])
h = 0
#print(d)

m = int(min(e[0]//d[0], e[1]//d[1], e[2]//d[2]))
p = int(max(e[0]//d[0], e[1]//d[1], e[2]//d[2]))
h += m
#print(m,p)
for i in range(m+1,p+2):
    n = ((i-m)*d[0])*f[0] + ((i-m)*d[1])*f[1] + ((i-m)*d[2])*f[2]
    if n-g>0.3:
        h += i-1
        print(h)
        #print(n,g)
        break
else:
    #print(h)
    g -= n
    h += p
    r = e[0]*f[0] + e[1]*f[1] + e[2]*f[2]
    h += g // r
    print(h)

