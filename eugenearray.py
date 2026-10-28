import sys
sys.stdin = open("main.in","r")
input(); array=[int(i) for i in input().split()]; 
prefix = [0]; pty=0; count=0
for i in range(len(array)): prefix.append(prefix[i]+array[i])
for ptx in range(len(array)):
    visited = set(); temp=0
    while pty<len(prefix) and prefix[pty] not in visited:
        visited.add(prefix[pty]); temp+=1; pty+=1
    count+=temp
print(count)
