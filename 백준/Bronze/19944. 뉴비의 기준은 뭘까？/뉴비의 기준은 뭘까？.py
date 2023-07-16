import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if b <= 2:
    print('NEWBIE!')
elif b <= a and b > 2:
    print('OLDBIE!')
else:
    print('TLE!')