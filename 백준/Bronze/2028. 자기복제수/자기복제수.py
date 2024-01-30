import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    result = int(''.join(list(str(n**2))[::-1][:len(str(n))][::-1]))

    if n == result:
        print('YES')
    else:
        print('NO')