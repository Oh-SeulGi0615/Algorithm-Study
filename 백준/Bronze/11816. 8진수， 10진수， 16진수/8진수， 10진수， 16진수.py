import sys
input = sys.stdin.readline

x = list(input().rstrip())

if x[0] == '0':
    if x[1] == 'x':
        print(int(''.join(x[2:]), 16))
    else:
        print(int(''.join(x[1:]), 8))
else:
    print(int(''.join(x[:])))