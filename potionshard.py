import sys
import heapq
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[1].split()]
c,d = 0,0
e = []
for i in b:
    c += i
    d += 1
    heapq.heappush(e,i)
    if c>=0:
        continue
    else:
        c += -heapq.heappop(e); d-=1
print(d)



