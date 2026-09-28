import sys
sys.stdin = open("main.in". "r")
for i in range(int(input())):
    value, count = (int(j) for j in input().split()); actl = value - (count-3)
    if actl%2==1: list = [1 for j in range(count-3)] + [1, actl//2, actl//2]
    elif actl%4 != 0: list = [1 for j in range(count-3)] + [2, actl//2-1, actl//2-1]
    else: list = [1 for j in range(count-3)] + [4, actl//2-2, actl//2-1]
    print(''.join(list))