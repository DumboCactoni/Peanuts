import sys
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
for i in range(len(a)):
    b=[int(j) for j in a[i].split()]
    if i%2==0: c=b[1]; d=b[2]
    else:
        g=0
        while True:
            e=0; f=0 #h
            if d<0: break
            if c-2*d<0: d=d-1; continue
            for j in range(c-2*d+1):
                if j+1<len(b): f=max(f,b[j]+b[j+1])
                e+=b[j]
                #h.append(b[j]) #
            e+=f*d; g=max(g,e); d=d-1 #h.append(f*d)
            # print(h) #
        print(g)

