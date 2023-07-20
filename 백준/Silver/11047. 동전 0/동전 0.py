import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)][::-1]

changes = k
coins = 0
for i in range(n):
    if arr[i] > k:
        pass
    else:
        a, b = divmod(changes, arr[i])
        coins += a
        changes = b

print(coins)