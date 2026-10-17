import sys
from collections import Counter
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    input(); array=[int(j) for j in input().split()]
    array=sorted(array); count=0; 
    tf=False; counter=Counter(array)
    for second in array:
        prevbig=array[-1]; 
        count=2; ans=[[prevbig, second]]
        counter[prevbig]-=1; counter[second]-=1
        for newbig in array[::-1]:
            if counter[newbig]==0: continue
            counter[newbig]-=1
            if counter[prevbig-newbig]>0:
                counter[prevbig-newbig]-=1
                ans.append([newbig, prevbig-newbig])
                prevbig=newbig; count+=2
            else: break
        counter=Counter(array)
        if count==len(array): 
            print("YES"); print(second+array[-1]); tf=True
            for i in ans: print(" ".join([str(j) for j in i]))
            break
    if not tf: print("NO")

