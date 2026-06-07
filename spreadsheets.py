import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a = a[1:]
for i in a:
    b = i.split()
    c = []; d = [True, b[0]) # global, temporary
    for j in range(1,len(b)):
        if ord(b[j])>64 != d[0]:
            