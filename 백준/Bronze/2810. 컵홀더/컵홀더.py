import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

total = n + 1
for i in range(n-1):
    if arr[i] == 'L' and arr[i+1] == 'L':
        total -= 1
        arr[i], arr[i+1] = 0, 0

if n >= total:
    print(total)
else:
    print(n)