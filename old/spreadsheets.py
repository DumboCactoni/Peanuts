import sys
import math
#sys.stdin = open("/storage/emulated/0/Github/peanuts/main.in","r")
a = sys.stdin.read().strip().split('\n'); a = a[1:]
for i in a:
    b = [j for j in i]
    c = []; d = [b[0]] # global, temporary
    for j in range(1,len(b)):
        if (ord(b[j])>=ord('A')) != (ord(d[0])>=ord('A')):
            c.append(d)
            d = [b[j]]
        else:
            d.append(b[j])
    c.append(d)
    
    if len(c)==4:
        e = [[],[]]
        c[1] = int("".join(c[1]))
        c[3] = int("".join(c[3]))
        while c[3]>0:
            c[3]-=1
            e[0].insert(0,chr( ord('A')+c[3]%26 ))
            c[3] //= 26
        e[1]=c[1]
        e[0] = "".join(e[0])
        e = [str(j) for j in e]
        print("".join(e))
        
        
    else:
        e = ['R', [], 'C', 0]
        c[1] = int("".join(c[1]))
        c[0] = "".join(c[0])
        e[1] = c[1]
        for j in c[0]:
            e[3]=e[3]*26 + ord(j)-ord('A')+1
        e = [str(j) for j in e]
        print("".join(e))
        
        
