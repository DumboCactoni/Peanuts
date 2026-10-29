import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    length, maxi = (int(j) for j in input().split()); 
    array=[int(j) for j in input().split()]
    already = [0]*(maxi*2+2); diff=[0]*(maxi*2+2); curr=0; best=float('inf')
    for num in range(length//2):
        corr = length-num-1
        already[array[num]+array[corr]]+=1
        diff[min(array[num], array[corr])+1]+=1
        diff[max(array[num], array[corr])+maxi+1]-=1
    for num in range(2, 2*maxi+2):
        curr+=diff[num]; best=min(best, 
        curr-already[num]+2*(length//2-curr))
    print(best)