### 200 confusing

##### kinematics dynamics dimensional analysis
- [ ] 1
- [ ] 3
- [ ] 5
- [ ] 36
- [ ] 37
- [ ] 38
- [ ] 40
- [ ] 41
- [ ] 64
- [ ] 65
- [ ] 66
- [ ] 84
- [ ] 86

- [ ] 2
- [ ] 7
- [ ] 8
- [ ] 12
- [ ] 13
- [ ] 24
- [ ] 32
- [ ] 33
- [ ] 34
- [ ] 35
- [ ] 37
- [ ] 38
- [ ] 39
- [ ] 70
- [ ] 73
- [ ] 77
- [ ] 78

- [ ] 15
- [ ] 57
- [ ] 58
- [ ] 59
- [ ] 76
- [ ] 77
- [ ] 126
- [ ] 139
- [ ] 142
- [ ] 185
- [ ] 199

##### gravitation mech
- [ ] 15
- [ ] 16
- [ ] 17
- [ ] 18
- [ ] 32
- [ ] 81
- [ ] 87
- [ ] 88
- [ ] 89
- [ ] 110
- [ ] 111
- [ ] 112
- [ ] 116

- [ ] 6
- [ ] 7
- [ ] 17
- [ ] 18
- [ ] 32
- [ ] 51
- [ ] 107

##### ***elasticity ropes***
- [ ] 9
- [ ] 10
- [ ] 11
- [ ] 14
- [ ] 25
- [ ] 26
- [x] 43
- [x] 44
- [x] 672
- [ ] 68
- [ ] 69

- [ ] 4
- [ ] 67
- [ ] 81
- [ ] 100
- [ ] 102
- [ ] 103
- [ ] 104
- [ ] 105
- [ ] 106
- [ ] 108


##### liquids surface tension
- [ ] 19
- [ ] 27
- [ ] 28
- [ ] 49
- [ ] 50
- [ ] 70
- [ ] 73
- [ ] 74
- [ ] 75
- [ ] 91
- [ ] 115
- [ ] 143
- [ ] 200

- [ ] 29
- [ ] 62
- [ ] 63
- [ ] 129
- [ ] 130
- [ ] 131
- [ ] 132
- [ ] 143
- [ ] 199


### codeforces
- [x] distinct char queries
- [ ] solve the maze
- [ ] caesars legions

- [ ] valid bfs
- [ ] greg and graph
- [ ] checkposts
- [ ] sleeping schedule
- [ ] george and job
- [ ] little girl max xor
- [ ] f=ma 2026

- [x] 22
- [x] 23

### notes
- [x] physics, chem, english
- [ ] chem lab report
- [ ] linear alg review hw

[[plans]]
[[september3]]
![[prisms#schedule]]

1 apush albemarle 206
2 physics
3 apchem cottage chem
4 linearalg albemarle 306
5 apbio cottage log bio lab
6 research albemarle 202 with app physics
7 study hall
8 english albemarle 210

##### code
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


