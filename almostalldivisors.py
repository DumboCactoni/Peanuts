import sys
#sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
for i in range(len(a)):
    if i%2==1:
        sortedinput = sorted([int(i) for i in a[i].split()])
        length = len(sortedinput); target = sortedinput[0]*sortedinput[-1]
        factorslist = []
        for potentialfactor in range(1,int(target**0.5)+1):
            if target%potentialfactor==0:
                factorslist += [potentialfactor, target//potentialfactor]
        sortedinput += [1, target]
        sortedinput=set(sortedinput); factorslist=set(factorslist)
        if factorslist==sortedinput: print(target)
        else: print(-1)


