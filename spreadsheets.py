import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a = a[1:]
for i in a:
    b = i.split()
    c = []; d = []
    for j in range(len(b)):
        if ord(b[i])