import sys
#sys.stdin = open("main.in","r")
temp = [0]*2+[1]*(10**5-1); primes=[]
for curr in range(2,10**5+1):
    if temp[curr]==0: continue
    else:
        explorer = curr*curr
        while explorer<=(10**5):
            temp[explorer]=0; explorer+=curr
for curr in range(len(temp)): 
    if temp[curr]==1: primes.append(curr)
def factor(val):
    temp = val; curr=0; currprime=primes[curr]; exponents=0; limit=int(val**0.5)
    while currprime <= limit:
        currprime = primes[curr]; curr+=1
        while temp%currprime==0: temp = temp//currprime; exponents+=1
    if temp>1: exponents+=1
    return exponents
for i in range(int(input())):
    x,y,target = (int(j) for j in input().split())
    exponents = factor(x)+factor(y)
    if target<=exponents and target>=2: print("YES")
    elif target==1 and (x%y==0 or y%x==0) and x!=y: print("YES")
    else: print("NO")
