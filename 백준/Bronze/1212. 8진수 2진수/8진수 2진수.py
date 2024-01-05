import sys
input = sys.stdin.readline

oct_a = '0o' + input().rstrip()
int_a = int(oct_a, 8)
bin_a = bin(int_a)

print(bin_a[2:])