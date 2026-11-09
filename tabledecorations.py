import sys
#sys.stdin = open("main.in","r")
array = [int(i) for i in input().split()]; array=sorted(array)
if array[2]<=2*(array[0]+array[1]):
    print(sum(array)//3)
else: print(array[0]+array[1])