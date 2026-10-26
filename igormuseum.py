import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
rows, columns, cases = (int(i) for i in input().split()); array=[]
for i in range(rows): array.append([j for j in input()])
globalvisited = [[0]*columns for i in range(rows)]; 
regionnum=1; counts=[0]
for i in range(cases):
    x,y = (int(j) for j in input().split()); x-=1; y-=1
    stack = [((-1,-1),(x,y))]; count=0
    if globalvisited[x][y]: 
        print(counts[globalvisited[x][y]]); continue 
    globalvisited[x][y]=regionnum
    while stack: 
        origin=stack.pop()[1]
        for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
            new = (origin[0]+dx, origin[1]+dy)
            if not array[new[0]][new[1]]: continue
            if array[new[0]][new[1]]=="." and (not 
            globalvisited[new[0]][new[1]]):
                stack.append((origin,new))
                globalvisited[new[0]][new[1]]=regionnum
            elif array[new[0]][new[1]]=="*": count+=1
    regionnum+=1; counts.append(count); print(count)
