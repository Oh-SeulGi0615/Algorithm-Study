import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    _ = input().rstrip()

    candy = 0
    a = int(input().rstrip())
    for _ in range(a):
        b = int(input())
        candy += b
    
    if candy % a == 0:
        print('YES')
    else:
        print('NO')