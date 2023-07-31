import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    c, v = map(int, input().split())

    x, y = divmod(c, v)

    print(f'You get {x} piece(s) and your dad gets {y} piece(s).')