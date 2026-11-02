import sys
from collections import defaultdict, deque
#sys.stdin = open("main.in","r")
nodes, edgenum = (int(i) for i in input().split()); stack=deque()
array=[0]+[i for i in input()]; graph=defaultdict(list); degs=[0]*(nodes+1)
for i in range(int(edgenum)):
    prev, curr = (int(j) for j in input().split())
    degs[curr]+=1; graph[prev].append(curr)
for node in range(1,nodes+1): 
    if degs[node]==0: stack.append(node)
freq=[[0]*26 for i in range(nodes+1)]; topo=[]; val=0
while stack:
    curr=stack.popleft(); currind=ord(array[curr])-ord("a")
    val = max(val, max(freq[curr]), freq[curr][currind]+1)
    for node in graph[curr]:
        degs[node]-=1
        if degs[node]==0: stack.append(node)
        for rel in range(26):
            freq[node][rel]=max(freq[node][rel], 
            freq[curr][rel]+1 if rel==currind else freq[curr][rel])
    topo.append(curr)
print(val if len(topo)==nodes else -1)
    