### 200 puzzling

##### ***gravitation mech***
hopefully by thursday, early friday
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
- [x] 25 
- [ ] 26
- [x] 43
- [x] 44
- [x] 67
- [x] 68
- [ ] 69

- [ ] 4
- [ ] 67
- [x] 81
- [x] 100	
- [x] 102
- [x] 103
- [x] 104
- [x] 105
- [ ] 106
- [x] 108


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
- [x] solve the maze
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

### bs
title, goal, chemicals/materials,  method description, brief procedures, well-organized data table, observation, calculation based on the balanced equation and stoichiometry, data analysis including error analysis

Title
Determining the mass percent of copper in brass ingots

Goal
By using a spectrophotometer, we can buid a calibration curve for copper nitrate produced by reaction with nitric acid. Copper nitrate has a blue color, while zinc nitrate is colorless.

Chemicals/materials
We use brass ingots, concentrated nitric acid, copper sulfate hydrate, a spectrophotometer, beakers, volumetric flasks, a micropipette and pipettes.

Procedure and observations
1. Measure out and dissolve 0.96g of brass ingots in concentrated nitric acid. A brown gas, nitrogen dioxide is observed, while the solution turns from colorless to green, and not yet blue, because of dissolved nitrogen dioxide.
2. Transfer aqueous brass and dilute to 100ml in volumetric flask. Rinse the erlenmyer as it is transferred.
3. Prepare 0.05, 0.1, 0.15 and 0.2M standard copper sulfate solutions. The solutions from least to most concentrated go from light to dark blue.
4. Analyze the full spectrum of copper sulfate to find the peak wavelength. Produce the calibration curve using this wavelength. Determine copper nitrate molarity in the brass solution.

Data and error analysis

### notes
- [x] physics, chem, english
- [ ] chem lab report
- [x] linear alg review hw
- [ ] english read
- [ ] physics online, hw

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

##### kinematics dynamics dimensional analysis
- [ ] 1
- [ ] 3
- [ ] 5
- [ ] 36
- [ ] 37
- [ ] 38
- [x] 40
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
- [x] 33
- [x] 34
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


