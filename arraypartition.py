import sys
import math
sys.stdin = open("main.in")
a = sys.stdin.read().strip().split('\n'); a=a[1:]
for i in range(len(a)):
    if i%2==0: array_length=int(a[i])
    if i%2==1:
        array = [int(j) for j in a[i].split()]
        possible_partition_sizes = [j for j in range(1,array_length+1) 
        if array_length%j==0] ## can use root
        num_of_valid_partition_sizes = 0
        for partition_size in possible_partition_sizes:
            gcd = 0
            for indice in range(array_length):
                offset=indice-partition_size
                if offset>=0:
                    gcd=math.gcd(gcd,abs(array[indice] - array[offset]))
            if gcd>1 or gcd==0: num_of_valid_partition_sizes += 1
        print(num_of_valid_partition_sizes)


