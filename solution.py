M = 1e9
d = [M]*3000
d[1] = 0
import sys
sys.stdin = open("main.in","r")
for i in range(1, 1001):
    for j in range(1, i//2+2):
        d[i//j+i] = min(d[i]+1, d[i//j+i])
print(d[:10])
for _ in range(int(input())):
    n,k=map(int,input().split())
    k=min(k,12*n)
    costs=[]
    l_b=list(map(int,input().split()))
    l_c=list(map(int,input().split()))
    dp=[0]*(k+1)
    for i in range(n):
        l=k
        while l>=d[l_b[i]]:
            dp[l]=max(dp[l],dp[l-d[l_b[i]]]+l_c[i])
            l-=1
    print(dp[k])