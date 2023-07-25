import sys
input = sys.stdin.readline

cnt = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break

    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = int(n1 / 2)
    else:
        n2 = int((n1 + 1) / 2)

    n3 = 3 * n2
    n4 = n3 // 9

    if n1 % 2 != 0:
        print(f'{cnt}. odd {n4}')
    else:
        print(f'{cnt}. even {n4}')

    cnt += 1