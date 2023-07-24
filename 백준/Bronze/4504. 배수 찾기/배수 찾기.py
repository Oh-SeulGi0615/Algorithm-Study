import sys
input = sys.stdin.readline

t = int(input())

while True:
    n = int(input())
    if n == 0:
        break

    if n % t == 0:
        print(f'{n} is a multiple of {t}.')
    else:
        print(f'{n} is NOT a multiple of {t}.')