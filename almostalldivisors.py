import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
for i in range(len(a)):
    if i%2==1:
        b = sorted([int(i) for i in a[i].split()]); c=len(b)
        
        if c%2==0:
            print(b[c//2]*b[c//2-1])
        else:
            print(b[c//2]**2)

