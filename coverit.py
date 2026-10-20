import sys
from collections import defaultdict, deque
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    vertices, edges = (int(j) for j in input().split())
    graph = defaultdict(list); stack=deque([[0,1]]); ones=[]
    visited={1}; color=[-1 for i in range(vertices+1)]; color[1]=0
    for j in range(edges):
        x, y = (int(k) for k in input().split())
        graph[x].append(y); graph[y].append(x)
    while stack:
        origin = stack.popleft()[1]
        for vertice in graph[origin]:
            if vertice not in visited:
                stack.append([origin, vertice])
                visited.add(vertice); color[vertice]=1-color[origin]
                if color[vertice]==1: ones.append(vertice)
    if len(ones)<vertices-len(ones): 
        print(len(ones)); print(" ".join([str(j) for j in ones]))
    else: 
        print(vertices-len(ones))
        zeros=[j for j in range(1,vertices+1) if color[j]==0]
        print(" ".join([str(j) for j in zeros]))        




