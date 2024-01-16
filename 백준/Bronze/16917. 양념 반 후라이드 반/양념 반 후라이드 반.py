import sys
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())

if a + b > c * 2:
    if x > y:
        if a < c * 2:
            price = (min(x, y) * 2 * c) + ((max(x, y) - min(x, y)) * a)
        else:
            price = x * 2 * c
    elif x < y:
        if b < c * 2:
            price = (min(x, y) * 2 * c) + ((max(x, y) - min(x, y)) * b)
        else:
            price = y * 2 * c

    else:
        price = x * 2 * c

else:
    price = (a * x) + (b * y)

print(price)