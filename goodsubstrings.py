import sys
from collections import defaultdict
#sys.stdin = open("main.in","r")
string = input(); bads = input(); maxi = int(input())
dictrie = dict(); curr = dictrie; ans=0
is_bad = [bads[ord(char)-ord("a")]=="0" for char in string]
for x in range(len(string)):
    curr = dictrie; bad=0
    for y in range(x, len(string)):
        if is_bad[y]: bad+=1
        if bad>maxi: break
        if string[y] not in curr: curr[string[y]]=dict(); ans+=1
        curr = curr[string[y]]
print(ans)


