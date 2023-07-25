import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [m]
for _ in range(n):
    a, b = map(int, input().split())

    m += a
    m -= b
    arr.append(m)

if min(arr) < 0:
    print(0)
else:
    print(max(arr))