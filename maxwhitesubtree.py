import sys
#sys.stdin = open("main.in","r")
vertices = int(input())
colors = [(int(i) if int(i)==1 else -1) for i in input().split()]
edges = dict(); dp=[0]*(vertices+1); rooted=dict()
for i in range(1,len(colors)+1): dp[i]=colors[i-1]
for i in range(vertices-1):
   x, y = (int(j) for j in input().split())
   if x not in edges: edges[x] = []; rooted[x]=[]
   if y not in edges: edges[y] = []; rooted[y]=[]
   edges[x].append(y); edges[y].append(x); 

stack=[1]; visited=set() # rooting tree
while stack:
   curr=stack.pop(); stack.extend(set(edges[curr])-visited)
   if curr in visited: continue
   visited.add(curr)
   rooted[curr].extend(set(edges[curr])-visited)

stack=[1]; visited = set() # creating dp
while stack:
   curr=stack.pop()
   if curr not in visited:
      visited.add(curr); stack.append(curr)
      stack.extend(set(rooted[curr])-visited)
   else: 
      for to in rooted[curr]: dp[curr]+=max(0,dp[to])

stack=[1]; visited=set(); best = [i for i in dp] # rerooting
while stack:
   curr=stack.pop(); stack.extend(set(edges[curr])-visited) # curr made root
   if curr in visited: continue
   visited.add(curr)
   for to in edges[curr]:
      if to not in visited: 
         best[to] = dp[to]+max(0,best[curr]-max(0,dp[to]))

print(" ".join([str(i) for i in best][1:]))


