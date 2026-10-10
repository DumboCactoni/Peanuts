import sys
sys.stdin = open("main.in","r")
size = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]; sums=[0]; j=0
for i in array: j+=i; sums.append(j)
dp = [[0]*size[0] for i in range(size[2]+1)]
for count in range(1,size[2]+1):
    for start in range(size[0]):
        if start+size[1]<len(sums):
            prev = max(0, start-size[1])
            dp[count][start] = max(dp[count-1][prev] + 
            sums[start+size[1]]-sums[start], dp[count][start-1])
        elif start<=size[1]:
            dp[count][start]=dp[count][start-1] + array[start]
print(dp[size[2]][size[0]-size[1]])