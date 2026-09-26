import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    size = int(input()); array = [0]+[int(j) for j in input().split()]
    visited=defaultdict(int); cycles=0; bamboos=0; order=0
    for indice in range(1,size+1):
        if visited[indice]==0:
            curr = indice; initialorder = order
            while visited[curr]==0: 
                visited[curr] = order; order+=1; curr=array[curr]
            if visited[curr] < initialorder: continue
            if order-visited[curr]==2: bamboos+=1
            else: cycles+=1
    print(min(1,bamboos)+cycles,cycles+bamboos)