import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

if b % c != 0:
    result1 = b // c + 1
else:
    result1 = b // c

if d % a != 0:
    result2 = d // a + 1
else:
    result2 = d // a

if result1 > result2:
    print('PLAYER A')
elif result1 < result2:
    print('PLAYER B')
else:
    print('DRAW')