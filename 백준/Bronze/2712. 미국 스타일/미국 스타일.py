import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    a = float(a)

    if b == 'kg':
        c = round(a * 2.2046, 4)
        d = 'lb'
    elif b == 'lb':
        c = round(a * 0.4536, 4)
        d = 'kg'
    elif b == 'l':
        c = round(a * 0.2642, 4)
        d = 'g'
    elif b == 'g':
        c = round(a * 3.7854, 4)
        d = 'l'

    print(f'{c:.4f}', d)