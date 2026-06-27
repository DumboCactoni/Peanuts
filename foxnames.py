import sys
sys.stdin = open("main.in","r")
a = sys.stdin.read().strip().split('\n'); a=a[1:]; b=[]
a = [[j for j in i] for i in a]