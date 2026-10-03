import sys
#sys.stdin = open("main.in","r")
size = int(input()); weights = [[0]*size for i in range(size)]
for x in range(size):
    rowweights = [int(i) for i in input().split()]
    for y in range(len(rowweights)):
        weights[x][y]=int(rowweights[y])
delorder = [int(i)-1 for i in input().split()][::-1]; sum=0; sol=[]; added=set()
for k in delorder:
    sum=0; added.add(k)
    weightsk = weights[k]
    for x in delorder:
        weightsx = weights[x]
        for y in delorder:
            weightsx[y] = min(weightsx[y], weightsx[k]+weightsk[y])
    for x in added:
        for y in added: sum+=weights[x][y]
    sol.append(sum)
print(' '.join([str(i) for i in sol][::-1]))

