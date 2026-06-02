import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[0].split()]; a=a[1:]
d = [] # blank spaces 

for i in range(len(a)):
    c = a[i].split()
    for j in range(len(c)):
        if c[j] == ".":
            d.append([i,j])
    a[i]=c
e = defaultdict(int)
f = [] # turned into wall
while len(f)<len(d)-a[2]:
    for i in range(1,len(f)+1):
        g = False
        for j in range(len(d)):
            if abs(f[-i][0] - d[j][0]) +\
            abs(f[-i][1]-d[j][1]) == 1\
            and e[d[j]]==0:
                f.append(d[j])
                e[d[j]] += 1
                g = True
                break
        if g:
            break
for i in f:
    a[i[0]][i[1]] = "X"
for i in a:
    print("".join(i))