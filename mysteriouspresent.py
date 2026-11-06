import sys
#sys.stdin = open("main.in","r")
num, minx, miny = (int(i) for i in input().split()); array=[]; rtemp=[]
for i in range(num): 
    x, y = (int(j) for j in input().split())
    if x>minx and y>miny: array.append([x,y,i+1])
array = sorted(array); dp=[1]*(len(array)); 
parent=[-1]*(len(array))
for curr in range(len(array)):
    for prev in range(curr):
        if (array[prev][0]<array[curr][0] and dp[prev]+1>dp[curr]
        and array[prev][1]<array[curr][1]): 
            dp[curr] = dp[prev]+1; parent[curr]=prev
if not array: print(0)
else: 
    curr = dp.index(max(dp))
    while curr!=-1: rtemp.append(array[curr][2]); curr=parent[curr]
    rtemp = [str(i) for i in rtemp]
    print(len(rtemp)); print(" ".join(rtemp[::-1]))