import sys
from collections import defaultdict, deque
#sys.stdin = open("main.in","r")
dict = defaultdict(list)
for i in range(int(input())-1): 
    list = [int(j) for j in input().split()]
    dict[list[0]].append(list[1]); dict[list[1]].append(list[0])
givenbfs = [0]+[int(i) for i in input().split()]
posgiven = [0 for i in range(len(givenbfs))]
for i in range(len(givenbfs)): posgiven[givenbfs[i]]=i
for adjacencies in dict.values(): 
    adjacencies.sort(key=lambda x:posgiven[x])
stack = deque([i for i in dict[1]]); mybfs = [0, 1]; visited = {1}
while stack:
    curr = stack.popleft(); mybfs.append(curr); visited.add(curr)
    stack += [i for i in dict[curr] if i not in visited]
if mybfs==givenbfs: print("Yes")
else: print("No")
