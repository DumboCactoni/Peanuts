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
    if c>=0 and i>=0:
        continue
    if c>=0 and i<0:
        heapq.heappush(e,-i)
        continue
    elif e and c-i+e[0] >= 0:
        c += -i+heapq.heappop(e); d-=1
        #print(i,c,d)
    else:
        #print(i,c,d)
        c-=i; d-=1
        #print(i,c,d,e,"skip")
print(d)



