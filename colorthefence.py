import sys
#sys.stdin = open("main.in","r")
available = int(input())
costs=[float('inf')]+[int(i) for i in input().split()]
mincost = min(costs)
for i in range(9,0,-1):
    if costs[i]==mincost: best=i; break
length = available//mincost
answer = [best]*length
available-=length*mincost; curr=0
for value in range(9, best,-1):
    if available>=costs[value]-mincost: 
        extra = min(available//(costs[value]-mincost), length-curr)
        answer[curr:curr+extra] = [value]*extra
        available-=extra*(costs[value]-mincost)
        curr += extra
        if curr==length: break
if not answer: print(-1)
else: print("".join([str(i) for i in answer]))
