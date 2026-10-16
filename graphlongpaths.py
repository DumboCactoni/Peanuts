import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
info = defaultdict(list); order=[]
vertices, edges = (int(i) for i in input().split())
for i in range(edges):
    line = [int(j) for j in input().split()]
    info[line[0]].append(line[1]); info[line[1]].append(line[0])
    order.append((line[0], line[1]))
stack=[(1,0)]; visited=set(); ans=[0]*2+[-1]*(vertices); 
tf=True; final=[]; curr=[]
while stack:
    temp, parent = stack.pop()
    while curr and curr[-1]!=parent: curr.pop()
    if temp in visited:
        if ans[temp]==ans[parent]: 
            tf=False; break
        else: continue
    curr.append(temp); visited.add(temp)
    for vertice in info[temp]:
        if ans[vertice]==-1: ans[vertice]=1-ans[temp]
        stack.append((vertice, temp))
if tf: 
    print("YES")
    for line in order: 
        if ans[line[1]]-ans[line[0]]<0: final.append(1)
        else: final.append(0); 
    print("".join([str(i) for i in final]))
else: print("NO")