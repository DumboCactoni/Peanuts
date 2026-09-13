import sys
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
a = [int(i) for i in a]
for i in a:
    if i<4:
        print(-1)
    else:
        b=[2*j+1 for j in range((i-1)//2, -1, -1)]; c=[4,2]
        c+=[2*j for j in range(3,i//2+1)]
        print(" ".join( [str(j) for j in b+c] ) )
