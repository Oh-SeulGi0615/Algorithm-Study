import sys
input = sys.stdin.readline

n = int(input())
bin_n = bin(n)

arr = list(map(int, str(bin_n)[2:]))[::-1]

result = 0
for i in range(len(arr)):
    result += (3 ** i) * arr[i]

print(result)