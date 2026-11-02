import sys
sys.stdin = open("main.in","r")
for i in range(int(input())):
    array = [i for i in input()]; globalcount=0
    for halflength in range(1,len(array)//2+1):
        count=0
        for val in range(halflength):
            if (array[val]==array[val+halflength] or
            array[val]=="?" or array[val+halflength]=="?"): count+=1
        if count==2*halflength: globalcount=max(globalcount, 2*halflength)
        for left in range(len(array)-halflength):
            if (array[left-1]==array[left+halflength-1] or
            array[left-1]=="?" or array[left+halflength-1]=="?"): count-=1
            if (array[left]==array[left+halflength] or
            array[left]=="?" or array[left+halflength]=="?"): count+=1
            if count==2*halflength: globalcount=max(globalcount, 2*halflength)
    print(globalcount)


