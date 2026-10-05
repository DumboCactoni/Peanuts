import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
num=int(input()); costs = [0]+[int(i) for i in input().split()]
pairs = int(input()); dict = defaultdict(list); rdict=defaultdict(list)
for i in range(pairs):
    pair = [int(j) for j in input().split()]
    rdict[pair[1]].append(pair[0])
    dict[pair[0]].append(pair[1])
reversestack = []; visited=set()
for origin in range(1,num+1):
    if origin not in visited:
        visited.add(origin); stack=[origin]
        while stack:
            curr=stack.pop()
            while dict[curr]:
                val = dict[curr].pop(); stack.append(curr)
                if val not in visited: 
                    visited.add(val); curr=val
            reversestack.append(curr)
visited=set(); finaldfs = []
for origin in reversestack[::-1]:
    if origin not in visited:
        visited.add(origin); stack=[origin]; path=[origin]
        while stack:
            curr = stack.pop()
            while rdict[curr]:
                val = rdict[curr].pop(); stack.append(curr)
                if val not in visited: 
                    visited.add(val); curr=val; path.append(val)
        finaldfs.append(path)
totalcost = 0; totalways = 1
for stronglist in finaldfs:
    strongcost = []; mincost=float('inf'); tempways=0
    for val in stronglist: 
        strongcost.append(costs[val])
        mincost = min(costs[val], mincost)
    for val in strongcost: 
        if val==mincost: tempways+=1
    totalcost += mincost; totalways = totalways*tempways%(10**9+7)
print(totalcost, totalways)


            

