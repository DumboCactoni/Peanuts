import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
input(); array=[int(i) for i in input().split()]; 
potential=defaultdict(int); ans=[]; count=0; final=0
for bit in range(21):
    for num in array:
        if (num>>bit)&1==1: potential[bit]+=1; count+=1
while count>0:
    curr=0
    for bit in range(21):
        if potential[bit]: potential[bit]-=1; count-=1; curr|=1<<bit
    ans.append(curr)
for val in ans: final+=val**2
print(final)
