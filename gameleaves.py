import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
a=[ [int(i) for i in a[k].split()] for k in range(1,len(a)) ]; b=0
for i in range(len(a)):
    if i==b: 
        e=a[i][0]; b=b+e; c=a[i][1]; d=defaultdict(list)
        if e==1: print("Ayush")
        continue
    d[a[i][0]].append(a[i][1])
    d[a[i][1]].append(a[i][0])
    if i==b-1: 
        #print(d)
        if len(d[c])==1: print("Ayush") #print("bald")
        elif e%2==0: print("Ayush")
        else: print("Ashish")

