import sys
sys.stdin = open("main.in","r")
horsemen, footmen, maxhorse, maxfoot = (int(i) for i in input().split())
dp = [[[0,0] for i in range(footmen+1)] for j in range(horsemen+1)]; dp[0][0][0] = 0
for horseleft in range(horsemen+1):
    for footleft in range(footmen+1):
        for numhorse in range(maxhorse):
            dp[horseleft][footleft][0]+= dp[horseleft-numhorse][footleft][1]
            dp[horseleft][footleft][1]+= dp[horseleft-numhorse][footleft][0]
        for numfoot in range(maxfoot):
            dp[horseleft][footleft][1]+= dp[horseleft][footleft-numfoot][0]
            dp[horseleft][footleft][0]+= dp[horseleft][footleft-numfoot][1]
print(max(dp[horsemen][footmen][1], dp[horsemen][footmen][0]))

