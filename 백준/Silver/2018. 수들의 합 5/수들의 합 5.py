import sys
input = sys.stdin.readline

n = int(input())

start, end = 0, 0
cnt = 0
arr = [i for i in range(1, n)]
while end < len(arr):
    if sum(arr[start:end+1]) == n:
        cnt += 1
        end += 1
    elif sum(arr[start:end+1]) < n:
        end += 1
    elif sum(arr[start:end+1]) > n:
        start += 1

print(cnt+1)