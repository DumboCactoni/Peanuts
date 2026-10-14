import sys
from collections import defaultdict
sys.stdin = open("main.in","r")
info = defaultdict(list); order=[]
vertices, edges = (int(i) for i in input().split())
for i in range(edges):
    line = [int(j) for j in input().split()]
    info[line[0]].append(line[1]); info[line[1]].append(line[0])
    order.append(sorted((line[0], line[1])))
stack=[1]; visited=set(); ans=[0]*(vertices+1); 
tf=True; parity=0; final=[]
while stack:
    curr=[]; temp=stack.pop()
    while temp not in visited: 
        stack+=info[temp]; curr.append(temp); 
        visited.add(temp); temp=stack.pop()
        if len(curr)>=2 and temp==curr[-2]: 
            temp=stack.pop()
            if temp not in info[curr[-1]]: break
        else: ans[temp]=1-ans[curr[-1]]
    print(curr)
    if temp in curr and (len(curr)-curr.index(temp))%2==1: 
        tf=False; break
if tf: 
    print("YES")
    print(ans)
    for line in order: 
        if ans[line[1]]-ans[line[0]]<0: final.append(1)
        else: final.append(0); print(ans[line[1]]-ans[line[0]])
    print("".join([str(i) for i in final]))
else: print("NO")