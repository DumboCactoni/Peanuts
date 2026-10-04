import sys
sys.setrecursionlimit(10**7)
n=int(input())
c=list(map(int,input().split()))
m=int(input())
g=[[] for _ in range(n)]
rg=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    u-=1;v-=1
    g[u].append(v)
    rg[v].append(u)
vis=[0]*n
o=[]
def dfs(u):
    vis[u]=1
    for v in g[u]:
        if not vis[v]:dfs(v)
    o.append(u)
for i in range(n):
    if not vis[i]:dfs(i)
vis=[0]*n
mod=10**9+7
ans=0
ways=1
def rdfs(u,comp):
    vis[u]=1
    comp.append(u)
    for v in rg[u]:
        if not vis[v]:rdfs(v,comp)
for u in reversed(o):
    if not vis[u]:
        comp=[]
        rdfs(u,comp)
        mn=min(c[v] for v in comp)
        cnt=sum(1 for v in comp if c[v]==mn)
        ans+=mn
        ways=ways*cnt%mod
print(ans,ways)
