import sys
sys.stdin = open("main.in","r")
for i in range(int(input())):
    size = int(input()); array = [0]+[int(j) for j in input().split()]
    visited=set(); cycles=[]; bamboos=[]
    for indice in range(1,size):
        if indice not in visited: 
            curr=[indice, array[indice]]; visited |= {indice}
        else: continue
        while curr[-1] not in visited:
            visited |= {curr[-1]}; curr.append(array[curr[-1]])
        if len(curr)==1: continue
        elif curr[-1]==curr[0] and len(curr)>3: cycles.append(curr)
        else: bamboos.append(curr)
    print(bamboos,cycles)
    bamboos, cycles = len(bamboos), len(cycles)
    print(cycles+min(bamboos,1), bamboos+cycles)