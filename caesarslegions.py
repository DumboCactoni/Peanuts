import sys
#sys.stdin = open("main.in","r")
horsemen, footmen, maxhorse, maxfoot = (int(i) for i in input().split())
dp = [[[0,0] for i in range(footmen+1)] for j in range(horsemen+1)]
dp[0][0][0] = 1; dp[0][0][1] = 1
for horseleft in range(horsemen+1):
    for footleft in range(footmen+1):
        for numhorse in range(1,maxhorse+1):
            if horseleft>=numhorse:
                dp[horseleft][footleft][1]+= dp[horseleft-numhorse][footleft][0]
        for numfoot in range(1,maxfoot+1):
            if footleft>=numfoot:
                dp[horseleft][footleft][0]+= dp[horseleft][footleft-numfoot][1]
print(int((dp[horsemen][footmen][1]+dp[horsemen][footmen][0])%10**8))

