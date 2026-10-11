import sys
#sys.stdin = open("main.in","r")
inputs = [int(i) for i in input().split()]
print(2**((inputs[0]^inputs[1]).bit_length())-1)