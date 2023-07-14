import sys
input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for x in range(k):
    a = int(input())
    arr.append(a)

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    elif cnt < n:
        end = mid - 1

print(end)