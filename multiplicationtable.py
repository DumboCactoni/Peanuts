import sys
#sys.stdin = open("main.in","r")
xsize, ysize, target = (int(i) for i in input().split())
a=0; c=xsize*ysize; b=(a+c)//2
while a<c:
    curr=0
    for x in range(1, xsize+1): curr+=min(ysize, b//x)
    if curr>=target: c=b; b=(a+c)//2
    if curr<target: a=b+1; b=(a+c)//2
print(a)



