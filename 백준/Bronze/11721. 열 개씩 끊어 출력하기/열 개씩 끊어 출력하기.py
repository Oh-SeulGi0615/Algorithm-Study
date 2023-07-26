import sys
input = sys.stdin.readline

a = input().rstrip()

while True:
    if len(a) >= 10:
        print(a[:10])
        a = a[10:]
    else:
        print(a)
        break