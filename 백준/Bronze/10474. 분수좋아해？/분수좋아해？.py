import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    x, y = divmod(a, b)
    print(f'{x} {y} / {b}')