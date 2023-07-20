import sys
input = sys.stdin.readline

arr = []
for _ in range(7):
    n = int(input())

    if n % 2 == 1:
        arr.append(n)

arr.sort()

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])