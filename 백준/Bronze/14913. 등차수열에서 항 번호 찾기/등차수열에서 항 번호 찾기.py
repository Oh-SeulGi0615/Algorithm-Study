import sys
input = sys.stdin.readline

a, d, k = map(int, input().split())

x, y = divmod((k-a), d)
if x < 0 or y != 0:
    print('X')
else:
    print((k-a) // d + 1)