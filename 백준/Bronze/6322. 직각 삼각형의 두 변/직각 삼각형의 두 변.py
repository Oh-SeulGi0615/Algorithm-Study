import sys
input = sys.stdin.readline

cnt = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    print(f'Triangle #{cnt}')
    if a == -1:
        if c**2 - b**2 > 0:
            a = (c**2 - b**2)**0.5
            print(f'a = {round(a,3):.3f}')
        else:
            print('Impossible.')
    
    elif b == -1:
        if c**2 - a**2 > 0:
            b = (c**2 - a**2)**0.5
            print(f'b = {round(b,3):.3f}')
        else:
            print('Impossible.')

    elif c == -1:
        if a**2 + b**2 > 0:
            c = (a**2 + b**2)**0.5
            print(f'c = {round(c,3):.3f}')
        else:
            print('Impossible.')
    
    cnt += 1
    print()