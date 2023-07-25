import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c, d, e = map(int, input().split())

    sum_ = (a * 350.34) + (b * 230.9) + (c * 190.55) + (d * 125.3) + (e * 180.9)
    print(f'${sum_:.2f}')