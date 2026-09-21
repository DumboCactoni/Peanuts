import sys
#sys.stdin = open("main.in","r")
input = sys.stdin.read().strip().split('\n')
input = [[int(i) for i in line.split()] for line in input]; ans=1
if input[0][0]>input[0][1]: print(0)
else:
    for leftindice in range(len(input[1])):
        for rightindice in range(leftindice+1, len(input[1])):
            ans *= abs(input[1][leftindice] - input[1][rightindice]); ans=ans%input[0][1]
    print(ans)