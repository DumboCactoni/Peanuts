import sys
#sys.stdin = open("main.in","r")
input(); array=[int(i) for i in input().split()]
arraysum=sum(array); tf=False
if arraysum%2==1: print(0)
else:
    dp=[[0]*(len(array)+1) for i in range(arraysum//2+1)]; dp[0][0]=1
    for currsum in range(arraysum//2+1):
        for indice in range(len(array)):
            dp[currsum][indice+1] = max(
            dp[currsum][indice], dp[currsum-array[indice]][indice]
            if currsum>=array[indice] else -1)
    for indice in dp[arraysum//2]:
        if indice==1: tf=True
    #print(dp)
    if not tf: print(0)
    else:
        print(1)
        while tf:
            for indice in range(len(array)):
                if array[indice]%2==1: print(indice+1); tf=False; break
                array[indice]=array[indice]//2

    
