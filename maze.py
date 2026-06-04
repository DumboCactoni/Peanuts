import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[0].split()]; a=a[1:]
d = [] # blank spaces 
for i in range(len(a)):
    c = [j for j in a[i]]
    for j in range(len(c)):
        if c[j] == ".":
            d.append([i,j])
    a[i]=c
z = set(tuple(i) for i in d)
e = set() #f seen
f = [d[0]]; o = [] # turned into wall
e.add(tuple(d[0]))

while len(e)<len(d):
    g = False
    for x,y in ((0,-1), (-1,0), (0,1), (1,0)):
        l =  x+f[-1][0]; m = y+f[-1][1]
        if (l,m) in z and (l,m) not in e:
            f.append([l,m])
            o.append([l,m])
            e.add((l,m))
            g = True
            break

    if not g:
        f.pop()

#print(f)
for i in range(len(o)-b[2], len(o)):
    j = o[i]
    a[j[0]][j[1]] = "X"
for i in a:
    print("".join(i)) 