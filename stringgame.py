import sys
#sys.stdin = open("main.in","r")
initial = [i for i in input()]; target=[i for i in input()]
deletions = [int(i) for i in input().split()]; 
x,y,z=0,len(deletions)//2,len(deletions)-1; #removals
state=[0]*(len(deletions)); temp = [i for i in initial]; removeorder=1
for deletion in deletions: state[deletion-1]=removeorder; removeorder+=1
while x!=z:
    curr=0
    for indice in range(len(state)):
        if curr==len(target): break
        if state[indice]>y and initial[indice]==target[curr]: curr+=1
    if curr>=len(target): x=y; y=(z-x+1)//2+x
    else: z=y-1; y=(z-x+1)//2+x
print(x)