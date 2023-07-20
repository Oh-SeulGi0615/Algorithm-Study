import sys
input = sys.stdin.readline

x, y = map(int, input().split())

arr = []
seven = (1000 / y) * x
arr.append(seven)

n = int(input())
for _ in range(n):
    i, j = map(int, input().split())

    price = (1000 / j) * i
    arr.append(price)

print(f'{min(arr):.2f}')