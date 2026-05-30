import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n')
b = [int(i) for i in a[0]]; a=a[1:]
d = []
for i in range(len(a)):
    c = a[i].split()
    for j in range(len(c)):
        if c[j] == ".":
            d.append([i,j])
print(d)
