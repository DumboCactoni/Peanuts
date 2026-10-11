import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    hot, cold, target = (int(i) for i in input().split())
    if target<=(cold+hot)/2: print(2)
    else:
        best = (target-hot)//(cold+hot-2*target)
        compare1 = abs(((best+1)*hot + best*cold)-target*(2*best+1))
        compare2 = abs(((best+2)*hot + (best+1)*cold)-target*(2*(best+1)+1))
        if compare1*(2*(best+1)+1)<=compare2*(2*best+1): print(2*best+1)
        else: print(2*(best+1)+1)