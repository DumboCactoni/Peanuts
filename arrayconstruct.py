import sys
import math as m
import heapq as h
from collections import defaultdict
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
a = [int(i) for i in a]
for i in a:
    b=[[] for j in range(i+1)]; h.heappush(b[i],[1,i]) # list of zero sequences
    d=[0 for j in range(i+1)]; g=1; c=[]; h.heappush(c,-i) #final, #, longest length
    while g<i+1:
        e = b[-c[0]][0]; h.heappop(b[-c[0]]); h.heappop(c)
        f = m.floor((e[0]+e[1])/2); 
        d[f] = g; g+=1; n = [(f-1)-e[0]+1, e[1]-(f+1)+1]
        h.heappush(b[n[0]], [e[0], f-1])
        h.heappush(b[n[1]], [f+1, e[1]])
        h.heappush(c, -n[0]); h.heappush(c, -n[1])
    d=[str(d[j]) for j in range(1,len(d))]; print(" ".join(d))







