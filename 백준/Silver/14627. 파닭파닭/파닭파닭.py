import sys

s, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(s)]

left, right = 1, max(arr)
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= c:
        best = mid
        left = mid + 1
    elif cnt < c:
        right = mid - 1

result = sum(arr) - (best * c)
print(result)