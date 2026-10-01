import sys
#sys.stdin = open("main.in","r")
def dfs(visited, curr, sequence, bad, walls, coord):
    stack = [curr]
    while stack:
        curr = stack.pop()
        if curr in visited or curr in walls or curr in bad: continue
        visited |= {curr}; sequence.append(curr)
        for change in ((1,0), (0,1), (-1,0), (0,-1)):
            temp = (curr[0]+change[0], curr[1]+change[1])
            if (temp[0]<0 or temp[0]>coord[0]-1 
            or temp[1]<0 or temp[1]>coord[1]-1): continue
            if temp not in bad and temp not in walls: 
                stack.append(temp)
for i in range(int(input())):
    coord = [int(j) for j in input().split()]; bool=True
    bad = set(); good=set(); visited=set(); walls = set()
    for rownum in range(coord[0]): 
        curr = [k for k in input()]
        for columnnum in range(len(curr)):
            if curr[columnnum]=="B": bad.add((rownum, columnnum))
            if curr[columnnum]=="G": good.add((rownum,columnnum))
            if curr[columnnum] == "#": walls.add((rownum, columnnum))
    for villain in bad:
        for change in ((1,0), (0,1), (-1,0), (0,-1)):
            temp = (villain[0]+change[0], villain[1]+change[1])
            if temp in good: bool=False; break
            if temp[0]>=0 and temp[1]>=0: walls.add(temp)
    if not bool: print("No"); continue
    dfs(visited, (coord[0]-1, coord[1]-1), [], bad, walls, coord)
    for pers in good: 
        if pers not in visited: bool=False; print("No"); break
    if bool: print("Yes")


