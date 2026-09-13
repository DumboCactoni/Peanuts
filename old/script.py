import sys
sys.stdin = open("main.in","r")
input = sys.stdin.read().strip().split('\n')
list=[question for line in input
for question in str(line).split(",")]
for question in list:
	print("- [ ]", question)
