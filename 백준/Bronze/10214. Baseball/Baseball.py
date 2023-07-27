import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = 0, 0

    for _ in range(9):
        x, y = map(int, input().split())
        a += x
        b += y
    
    if a > b:
        print('Yonsei')
    elif b < a:
        print('Korea')
    else:
        print('Draw')