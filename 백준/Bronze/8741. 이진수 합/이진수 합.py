import sys
input = sys.stdin.readline

k = int(input())

max_int = 2**k - 1
int_sum = int(((max_int+1) * max_int) // 2)
bin_num = bin(int_sum)

print(bin_num[2:])