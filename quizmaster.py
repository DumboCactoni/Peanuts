import sys
#sys.stdin = open("main.in","r")
n=10**5; factors=[[] for i in range(n+1)]
for curr in range(1,n+1):
    temp=curr
    while temp<=n: factors[temp].append(curr); temp+=curr
for i in range(int(input())):
    length, lim = (int(j) for j in input().split())
    array = [int(j) for j in input().split()]; array=sorted(array); y=0
    helpers = [0]*(lim+1); count=0; diff=float("inf")
    for x in range(length):
        if x>0:
            prev=array[x-1]
            for factor in factors[prev]:
                if factor>lim: break
                helpers[factor]-=1
                if helpers[factor]==0: count-=1
        while count<lim and y<length:
            for factor in factors[array[y]]: 
                if factor>lim:break
                if helpers[factor]==0: count+=1
                helpers[factor]+=1
            y+=1
        if count>=lim: diff=min(diff, array[y-1]-array[x])
    print(diff if diff!=float("inf") else -1)
