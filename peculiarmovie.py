import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    num = int(input()); lines=set(); tf=False
    for i in range(num):
        line=input(); lines.add(line)
        if tf: continue
        if len(line)==1: tf=True
        if len(line)==2:    
            if line[::-1] in lines: tf=True
            for ind in range(ord("a"),ord("z")+1): 
                if line[::-1]+chr(ind) in lines: tf=True
        if len(line)==3:
            if line[::-1] in lines: tf=True
            if line[:0:-1] in lines: tf=True
    print("YES" if tf else "NO")