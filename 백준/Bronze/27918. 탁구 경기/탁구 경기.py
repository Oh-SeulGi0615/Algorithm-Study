import sys
input = sys.stdin.readline

n = int(input())

x, y = 0, 0
for _ in range(n):
    a = input().rstrip()
    if a == 'D':
        x += 1
    else:
        y += 1

    if x == y + 2 or y == x + 2:
        break

print(f'{x}:{y}')