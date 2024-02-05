import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = [i for i in range(min(a, b)+1, max(a, b))]

if max(a, b) - min(a, b) > 1:
    print(max(a, b) - min(a, b) - 1)
    print(*arr)
else:
    print(0)