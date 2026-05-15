import sys
import heapq
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[1].split()]
c,d = 0,0
e = []
for i in b:
    c += i
    d += 1
    if i<0:
        heapq.heappush(e,i)
    if c>=0:
        #print(i,c)
        continue
    elif e[0]<i:
        d -= 1
        c += -e[0]
    #print(i,c)
print(d)



