import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    rows, columns = (int(j) for j in input().split())
    info=[]; mindp=[[0]*columns for j in range(rows)]; 
    maxdp=[[0]*columns for j in range(rows)]
    for j in range(rows): 
        info.append([int(k) for k in input().split()])
    mindp[0][0]=info[0][0]; maxdp[0][0]=info[0][0]
    for row in range(rows):
        for column in range(columns):
            if row==0 and column==0: continue       
            mindp[row][column]=info[row][column]+min(
            mindp[row-1][column] if row else float("inf"), 
            mindp[row][column-1] if column else float("inf"))
            maxdp[row][column]=info[row][column]+max(
            maxdp[row-1][column] if row else -float("inf"), 
            maxdp[row][column-1] if column else -float("inf"))
    #pprint(mindp, maxdp)
    if ((rows+columns)%2==1 and 
    mindp[rows-1][columns-1]<=0 and maxdp[rows-1][columns-1]>=0):
        print("YES")
    else: print("NO")
