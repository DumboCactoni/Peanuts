import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]; b=[]
a = [[j for j in i] for i in a]; b=[]
for i in range(1,len(a)):
    c=False
    for j in range(min(len(a[i-1]), len(a[i]))):
        if a[i][j]!=a[i-1][j]: 
            b.append([a[i-1][j], a[i][j]]); break; c=True
    if c: continue
    elif len(a[i-1][j])>len(a[i][j]): print("Impossible"); sys.exit()
print(b)

    