import sys
from bisect import bisect_left as left, bisect_right as right
#sys.stdin = open("main.in", "r")
array = [0]+[i for i in input()]
info = [[0] for j in range(26)]
for index in range(1, len(array)): info[ord(array[index])-ord('a')].append(index)
for i in range(int(input())):
    line = [j for j in input().split()]; line[0] = int(line[0])
    targetindex, newletter = int(line[1]), line[2]
    if line[0]==1 and array[targetindex] != newletter: 
        oldinfoindex = ord(array[targetindex])-ord('a')
        newinfoindex = ord(newletter)-ord('a'); array[targetindex]=newletter
        oldinfosub = left(info[oldinfoindex], targetindex)
        del info[oldinfoindex][oldinfosub]
        newinfosub = left(info[newinfoindex], targetindex)
        info[newinfoindex].insert(newinfosub, targetindex)
    if line[0]==2:
        distinct = 0; start, end = int(line[1]), int(line[2])
        for letter in info:
            if right(letter, end) > left(letter, start): distinct += 1
        print(distinct)
