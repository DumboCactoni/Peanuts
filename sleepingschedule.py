import sys
#sys.stdin = open("main.in","r")
entry = [int(i) for i in input().split()]
durations = [int(i) for i in input().split()]; length = len(durations)
dp = [[0]*(length+1)for i in range(length)]; total=0
for index in range(length):
    total += durations[index]
    for stretches in range(index+1):
        ifstretch = (total-stretches-1)%entry[1]
        if ifstretch>=entry[2] and ifstretch<=entry[3]:
            dp[index][stretches+1] = max(
            dp[index][stretches+1], 1+dp[index-1][stretches])
        else: 
            dp[index][stretches+1] = max(
            dp[index][stretches+1], dp[index-1][stretches])
        ifnotstretch = (total-stretches)%entry[1]
        if ifnotstretch>=entry[2] and ifnotstretch<=entry[3]:
            dp[index][stretches] = max(
            dp[index][stretches], dp[index-1][stretches]+1)
        else: 
            dp[index][stretches] = max(
            dp[index][stretches], dp[index-1][stretches])
print(max(dp[length-1]))