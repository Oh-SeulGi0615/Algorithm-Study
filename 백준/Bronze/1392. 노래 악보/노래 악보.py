import sys
input = sys.stdin.readline

n, q = map(int ,input().split())
arr = [0]
for _ in range(n):
    t = int(input())
    arr.append(arr[-1] + t)

time = [int(input()) for _ in range(q)]

for i in time:
    for j in range(1, len(arr)):
        if arr[j-1] <= i < arr[j]:
            print(j)