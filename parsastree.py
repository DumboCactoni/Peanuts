import sys
sys.stdin = open("main.in","r")
input = sys.stdin.read().strip().split('\n'); input=input[1:]
def dfs(adjlist, origin, curr): 
    for newadj in adjlist[curr]:
        if newadj != origin:
            dfs(adjlist, curr, newadj)
    traversal.append([curr, origin])
nextcase = 0
for linenum in range(len(input)):
    if linenum==nextcase: 
        currcase=int(input[linenum]); nextcase+=2*int(input[linenum])
        verticeinfo=[]; pointinfo=[0]; continue
    if linenum < nextcase-currcase+1: 
        pointinfo.append([int(i) for i in input[linenum].split()])
    else: verticeinfo.append([int(i) for i in input[linenum].split()])
    if linenum==nextcase-1:
        adjlist = [[] for i in range(currcase+1)]
        for i,j in verticeinfo: adjlist[i].append(j); adjlist[j].append(i)
        #print(pointinfo, verticeinfo, adjlist)
        traversal = []; dfs(adjlist, 0, 1)
        dp = [[0,0] for i in range(len(traversal)+1)]
        print(traversal)
        for edge in traversal:
            if edge[1]==0: continue
            dp[edge[1]][0] += max(
            dp[edge[0]][0] + abs(pointinfo[edge[1]][0] - pointinfo[edge[0]][0]),
            dp[edge[0]][1] + abs(pointinfo[edge[1]][0] - pointinfo[edge[0]][1])
            )

            dp[edge[1]][1] += max(
            dp[edge[0]][0] + abs(pointinfo[edge[1]][1] - pointinfo[edge[0]][0]),
            dp[edge[0]][1] + abs(pointinfo[edge[1]][1] - pointinfo[edge[0]][1])
            )
        print(max(dp[1][0], dp[1][1]))



