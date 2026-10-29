import sys
import math
#sys.stdin = open("main.in","r")
input = sys.stdin.readline
for i in range(int(input())):
    num=int(input())
    if num%2==1: print("Bob")
    elif 2**int(math.log(num,2))==num:
        power = math.log(num,2)
        if power%2==0: print("Alice")
        else: print("Bob")
    else: print("Alice")