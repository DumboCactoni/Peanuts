import sys
import math
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[1].split()]; d = []
c = [int(i) for i in a[2].split()]; e = []
for i in range(1,len(b)):
    d.append(b[i]-b[0])
d = math.gcd(d)
for i in c:
    e.append(math.gcd(d,i))
print(e)
