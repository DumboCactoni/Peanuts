import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    input(); beauty = [int(j) for j in input().split()]
    dp = [0,0,0]
    for curr in range(len(beauty)):
        dp[2] = max(dp[2], dp[1]+beauty[curr]-curr)
        dp[1] = max(dp[1], dp[0]+beauty[curr])
        dp[0] = max(dp[0], beauty[curr]+curr)
    print(dp[2])