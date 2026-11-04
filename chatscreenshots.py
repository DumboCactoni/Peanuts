import sys
from collections import defaultdict, deque
#sys.stdin = open("main.in","r")
for i in range(int(input())):
	people, lines = (int(i) for i in input().split()); 
	graph=defaultdict(list); deg=[1]+[0]*(people); stack=deque(); cnt=0
	for j in range(int(lines)):
		line = [int(k) for k in input().split()][1:]
		for val in range(len(line)-1): 
			graph[line[val+1]].append(line[val]); deg[line[val]]+=1
	for d in range(len(deg)): 
		if deg[d]==0: stack.append(d)
	while stack:
		curr = stack.pop()
		for val in graph[curr]: 
			deg[val]-=1
			if deg[val]==0: stack.append(val)
		cnt+=1
	print("YES" if cnt==people else "NO")