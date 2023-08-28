import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

cnt = 0
for i in range(1,len(arr)):
    if arr[i] != i:
        cnt += 1

print(cnt)