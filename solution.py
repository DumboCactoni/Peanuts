import sys
R=iter(sys.stdin.read().split())
S=lambda:next(R)
I=lambda:int(S())
r=range
A=[ord(c)-97for c in S()]
n=len(A)
T=[[0]*(n+1)for _ in r(26)]
def u(x,i,d):
	while i<=n:T[x][i]+=d;i+=i&-i
def p(x,i):
	r=0
	while i:r+=T[x][i];i&=i-1
	return r
for i in r(n):u(A[i],i+1,1)
for _ in r(I()):
	if I()==1:i=I();u(A[i-1],i,-1);A[i-1]=ord(S())-97;u(A[i-1],i,1)
	else:i,j=I(),I();print(sum(p(x,i-1)!=p(x,j)for x in r(26)))