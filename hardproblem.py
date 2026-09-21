import sys
#sys.stdin = open("main.in","r")
input = sys.stdin.read().strip().split('\n')
costs = [int(i) for i in input[1].split()]; lines=input[2:]
dp = [[float("inf"), float("inf")] for i in range(len(lines))]
dp[0][0]=0; dp[0][1]=costs[0]
for line in range(1,len(lines)):
    for toflip in range(2):
        if lines[line][::-1 if toflip else 1] >= lines[line-1][::]: 
            dp[line][toflip] = min(dp[line][toflip], 
            dp[line-1][0] + costs[line]*toflip)
        if lines[line][::-1 if toflip else 1] >= lines[line-1][::-1]:
            dp[line][toflip] = min(dp[line][toflip], 
            dp[line-1][1] + costs[line]*toflip)

if min(dp[len(lines)-1][0], dp[len(lines)-1][1]) == float("inf"): print(-1)
else: print( min(dp[len(lines)-1][0], dp[len(lines)-1][1]) )