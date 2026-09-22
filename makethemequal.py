import sys
sys.stdin = open("main.in","r")
globalcosts = [float("inf") for i in range(1001)]
for cost in range(1,1001):
    for divisor in range(1,cost+1):
        globalcosts[cost+cost//divisor] = min(globalcosts[cost+cost//divisor], 
        1+globalcosts[cost])
for indice in range(int(input()):
    maxop = [int(i) for i in input().split()][1]
    array = [int(i) for i in input().split()]; prizes = [int(i) for i in input().split()]
    costs = [globalcosts[i] for i in array]
    dp = [[0, 0] for i in range(len(localcosts)+1)]
    for index in range(len(costs)):
        if dp[index-1][1] + costs[index] < maxop: 
            dp[index][0] = dp[index-1][1]; dp[index]
        elif dp[index-1]:
            dp[index][0] = max(dp[index-1][0], dp[index][0]-prizes[index-1]+prizes[index])



