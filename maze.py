import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[0].split()]; a=a[1:]
d = []
for i in range(len(a)):
    c = a[i].split()
    for j in range(len(c)):
        if c[j] == ".":
            d.append([i,j])
e = defaultdict(int)
f = []
while len(f)<len(d)-a[2]:
    for i in range(1,len(f)+1):
        for j in range(len(d)):
            if f[-i][0]+1==d[j][0] and f[-1][1]==d[j][1] and :
                f.append(d[j])
                e[f[i]]    


    
