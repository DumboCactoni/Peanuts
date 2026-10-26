import sys
#sys.stdin = open("main.in","r")
signs, length, remove = (int(i) for i in input().split())
pos = [int(i) for i in input().split()]+[length]
array = [int(i) for i in input().split()]
dp = [[float("inf")]*(remove+1) for i in range(signs+1)]
dp[0][0]=0
for curr in range(1,signs+1):
    if curr!=0:
        dp[curr][0]=dp[curr-1][0]+(
        pos[curr]-pos[curr-1])*array[curr-1]
    for removals in range(1,remove+1):
        for prev in range(max(0,curr-1-removals),curr):
            dp[curr][removals]=min(dp[curr][removals],
            dp[prev][removals-(curr-prev-1)]+
            (pos[curr]-pos[prev])*array[prev])
print(min(dp[signs]))
