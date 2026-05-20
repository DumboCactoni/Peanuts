import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
a = [int(i) for i in a[0].split()]
b = [[0,0] for i in range(a[0]+1)]
b[0][0]=1
for i in range(1,a[0]+1):
    for j in range(n-a[2],i):
        b[i][0]+=b[j][0]
        b[i][1]+=b[j][1]
    for j in range(n-a[2]):
        b[i][1]+=b[j][0]+b[j][1]
print(b[a[0]][1])