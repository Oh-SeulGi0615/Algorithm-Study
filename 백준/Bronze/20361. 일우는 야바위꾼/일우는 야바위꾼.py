import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
arr = [0 if i != (x-1) else 1 for i in range(n)]

for s in range(k):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(arr.index(1)+1)