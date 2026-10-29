import sys
#sys.stdin = open("main.in","r")
input(); array=[int(i) for i in input().split()]; 
prefix = [0]; pty=0; count=0; ptx=0; visited=set()
for i in range(len(array)): prefix.append(prefix[i]+array[i])
while pty<len(prefix):
    while pty<len(prefix) and prefix[pty] not in visited:
        visited.add(prefix[pty]); count+=pty-ptx; pty+=1
    while pty<len(prefix) and prefix[pty] in visited:
        visited.remove(prefix[ptx]); ptx+=1
print(count)
