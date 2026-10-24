import sys
import math
#sys.stdin = open("main.in","r")
n=5*10**6; smolfactor=[0]*(n+1); count=[0]*(n+1)
for num in range(2,int(n**0.5)+1):
    if smolfactor[num]!=0: continue
    curr=num
    while curr<=n: smolfactor[curr]=num; curr+=num
for num in range(2,n+1): 
    count[num]= count[num//(smolfactor[num] or num)]+1
for num in range(3,n+1): count[num]+=count[num-1]
for i in range(int(input())):
    a,b = (int(j) for j in input().split())
    print(count[a]-count[b])
