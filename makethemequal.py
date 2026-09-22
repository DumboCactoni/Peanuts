import sys
sys.stdin = open("main.in","r")
input = sys.stdin.read().strip().split('\n'); input=input[1:]
for indice in range(len(input)):
    line = input[indice]; line = [int(i) for i in line.split()]
    if indice%3==0: target = line[0]; maxop = line[1]
    elif indice%3==1: array=line
    else:
        prizes=line; dp = [float("inf") for i in range(target)] + [0]
        for subtarget in range(target, 0, -1):
            for divisor in range(1, target+1):
                if subtarget-target//subtarget>0: 
                    dp[subtarget-target//subtarget] = min(
                    dp[subtarget-target//subtarget], 1+dp[subtarget])
                    dp[subtarget+subtarget//divisor] = min(
                    dp[subtarget+subtarget//divisor], 1+dp[subtarget])
        print(dp)
        







        #dp=[[0,0,0] for i in range(len(array))] #maxcoins w/ vs w/o
        #for value in range(len(array)):
            #if dp[value-1][2]==maxop:
                #dp[value][0] = max(dp[value-1][1]+)