import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
info = defaultdict(list); order=[]
vertices, edges = (int(i) for i in input().split())
for i in range(edges):
    line = [int(j) for j in input().split()]
    info[line[0]].append(line[1]); info[line[1]].append(line[0])
    order.append(sorted((line[0], line[1])))
stack=[1]; curr=[1,0]; visited=set(); 
ans=defaultdict(int); tf=True; parity=0; final=[]
while len(visited)!=vertices:
    length=0
    while curr[0] not in visited: 
        visited.add(curr[0]); stack+=info[curr[0]]; 
        curr[1]=stack.pop(); length+=1
        ans[curr[1]]=1-ans[curr[0]]; curr[0]=curr[1]
    if curr[0] in visited and length%2==0: 
        curr[0]=stack.pop(); continue
    else: tf = False; break
if tf: 
    print("YES")
    for line in order: 
        if ans[line[1]]-ans[line[0]]==1: final.append(0)
        else: final.append(1)
    print("".join(final[1:]))
else: print("NO")