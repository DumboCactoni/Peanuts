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
#print(m,p)
for i in range(m+1,p+2): # i iterates across number of burgers
    n = 0
    for j in range(3):
        x = f[j]*(i*d[j]-e[j]) if f[j]*(i*d[j]-e[j])>0 else 0
        n += x
    #print(i,n)
    if n-g>0.3:
        h += i-1
        print(h)
        #print(n,g)
        sys.exit()
#print(h)
g -= n
h += p+1
r = e[0]*f[0] + e[1]*f[1] + e[2]*f[2]
h += g // r
print(h)