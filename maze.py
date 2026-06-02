import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[0].split()]; a=a[1:]
d = [] # blank spaces 
for i in range(len(a)):
    c = [j for j in a[i]]
    for j in range(len(c)):
        if c[j] == ".":
            d.append([i,j])
    a[i]=c
e = defaultdict(int)

f = [d[0]] # turned into wall
while len(f)<b[2]+1:
    for i in range(1,len(f)+1):
        g = False
        for j in range(len(d)):
            if abs(f[-i][0] - d[j][0]) +\
            abs(f[-i][1]-d[j][1]) == 1\
            and e[tuple(d[j])]==0:
                f.append(d[j])
                e[tuple(d[j])] += 1
                g = True
                break
        if g:
            break

for i in f:
    a[i[0]][i[1]] = "X"
for i in a:
    print("".join(i))