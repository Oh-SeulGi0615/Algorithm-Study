import sys
input = sys.stdin.readline

sum = 0
arr = []
for _ in range(4):
    a, b = map(int, input().split())
    sum += b - a
    arr.append(sum)

print(max(arr))