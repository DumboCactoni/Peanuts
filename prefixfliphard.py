import sys
#sys.stdin = open("main.in","r")
for i in range(int(input())):
    input(); seq1 = [j for j in input()]
    seq2 = [j for j in input()]; ans1=[]; ans2=[]
    for val in range(len(seq1)-1):
        if seq1[val]!=seq1[val+1]: ans1.append(str(val+1))
    if seq1[-1]=="1": ans1.append(str(len(seq1)))
    for val in range(len(seq2)-1):
        if seq2[val]!=seq2[val+1]: ans2.append(str(val+1))
    if seq2[-1]=="1": ans2.append(str(len(seq2)))
    if seq1==seq2: print(0)
    else: ans = ans1+ans2[::-1]; print(len(ans)," ".join(ans))