import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    result += int(round(i / 2 + 0.0001, 0))

if result >= n:
    print('YES')
else:
    print('NO')