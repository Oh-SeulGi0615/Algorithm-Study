import sys
input = sys.stdin.readline

n = 1
while True:
    a, b, c = map(float, input().split())
    if b == 0.0:
        break
    distance = round((a * 3.1415927 * b) / 12 / 5280, 2)
    hour = round((a * 3.1415927 * b) / 12 / 5280 / c * 3600, 2)

    print(f'Trip #{n}: {distance:.2f} {hour:.2f}')
    n += 1