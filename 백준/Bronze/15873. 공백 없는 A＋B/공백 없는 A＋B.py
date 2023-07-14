import sys
input = sys.stdin.readline

n = list(input().rstrip())

if len(n) == 2:
    a = int(n[0])
    b = int(n[1])
    print(a+b)
elif len(n) == 3:
    if int(n[1]) == 0:
        a = int(n[0] + n[1])
        b = int(n[2])
        print(a+b)
    else:
        a = int(n[0])
        b = int(n[1] + n[2])
        print(a+b)
else:
    a = int(n[0] + n[1])
    b = int(n[2] + n[3])
    print(a+b)