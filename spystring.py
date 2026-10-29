import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    rows, columns = (int(j) for j in input().split()); array=[]
    for j in range(rows): array.append([k for k in input()]); tf=False
    for curr in range(len(array[0])):
        if tf: break
        for chrindex in range(ord('a'), ord('z')+1):
            temp=array[0][:]; tf=True
            if array[0][curr]!=chr(chrindex): temp[curr]=chr(chrindex)
            for test in array[1:]:
                diff=0
                for currtest in range(len(test)):
                    if test[currtest]!=temp[currtest]: diff+=1
                if diff>1: tf=False; break
            if tf: print("".join(temp)); break
    if not tf: print(-1)
            

