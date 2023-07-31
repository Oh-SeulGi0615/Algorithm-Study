import sys
input = sys.stdin.readline

while True:
    m, a, b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        break

    time = round((m/a - m/b) * 3600)

    x, c = divmod(time, 3600)
    y, z = divmod(c, 60)

    print(f'{x}:{str(y).zfill(2)}:{str(z).zfill(2)}')