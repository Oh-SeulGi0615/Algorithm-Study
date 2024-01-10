import sys
input = sys.stdin.readline

n = int(input())
x, y = divmod(n, 2)

if y > 0:
    print('CY')
else:
    print('SK')