import sys
#sys.stdin = open("main.in","r")
globalcosts = [float("inf") for i in range(1001)]; globalcosts[1] = 0
for cost in range(1,1001):
    for divisor in range(1,cost+1):
        if cost+cost//divisor<1001:
            globalcosts[cost+cost//divisor] = min(
            globalcosts[cost+cost//divisor], 1+globalcosts[cost])
for indice in range(int(input())):
    maxop = [int(i) for i in input().split()][1]
    maxop = min(maxop, 12*[int(i) for i in input().split()][0])
    array = [int(i) for i in input().split()]
    prizes = [int(i) for i in input().split()]
    costs = [globalcosts[i] for i in array]
    dp = [0 for i in range(maxop+1)]
    for index in range(len(array)):
        opleft = maxop
        while opleft >= costs[index]:
            dp[opleft] = max(dp[opleft], 
            dp[opleft-costs[index]]+prizes[index]); opleft -= 1
    print(dp[maxop]. print(maxop))


