import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 1
for i in range(n):
    result *= arr[i] % m

print(result % m)