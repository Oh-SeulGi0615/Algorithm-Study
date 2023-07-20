import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cnt = 0
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    if a >= n:
        cnt += 1
    else:
        price = n - a
        arr.append(price)

arr.sort()
print(sum(arr[:(m-1) - cnt]))