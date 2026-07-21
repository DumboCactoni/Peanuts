import sys
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); b=int(a[0])
a = [int(i) for i in a[1].split()]; e=max(a)
c = [False for i in range(e+1)]; d = [] # primes
for i in range(2,e+1):
    if not c[i]: d.append(i)
    for j in d: 
        if j*i>e: break
        c[i*j]=True
        if i%j==0: break

a1=1
for i in d:
    h = []; g=0 #power, number of zeros
    for j in a:
        f=0; b1=j
        while b1%i==0:
            b1=b1//i; f+=1
        if f==0: g+=1
        if g==2: break
        h.append(f)
    if g>=2: continue
    h=sorted(h); a1=a1*(i**h[1])
    #print(h)
print(a1)

