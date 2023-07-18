import sys
input = sys.stdin.readline

a = int(input())

sum1 = 0
for _ in range(a):
    n = int(input())
    sum1 += n

if sum1 > 0:
    print('+')
elif sum1 < 0:
    print('-')
else:
    print(0)

b = int(input())

sum2 = 0
for _ in range(b):
    n = int(input())
    sum2 += n

if sum2 > 0:
    print('+')
elif sum2 < 0:
    print('-')
else:
    print(0)

c = int(input())

sum3 = 0
for _ in range(c):
    n = int(input())
    sum3 += n

if sum3 > 0:
    print('+')
elif sum3 < 0:
    print('-')
else:
    print(0)