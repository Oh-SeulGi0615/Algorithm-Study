import sys
input = sys.stdin.readline

while True:
    a = int(input())
    if a == 0:
        break

    b = list(str(a))
    b_reverse = b[::-1]

    if b == b_reverse:
        print('yes')
    else:
        print('no')