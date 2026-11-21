import sys
sys.stdin = open("main.in","r")
for i in range(int(input())):
   length = int(input()); tf=False
   array = [int(i) for i in input().split()]
   for pos in range(1,length):
      if array[pos]==array[pos-1]: tf=True; break
   if len(set(array))==1: print(1); print([1]*length)
   elif length%2==0: 
      print(2); print([1,2]*length//2)
   elif tf: 
      print(2); output=[]
      for ind in range(length):
         if ind==pos: output.append(output[-1])
         else: output.append(1 if output[-1]==2 else 2)
      print(" ".join(str(i) for i in output))
   else: print(3); print([1,2]*length//2+[3])