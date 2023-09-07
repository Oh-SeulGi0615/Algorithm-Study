import sys
input = sys.stdin.readline

k = int(input())
d1, d2 = map(int, input().split())

if d1 == d2:
    print(k**2)
else:
    d3 = (d1 - d2) / 2

    if d3 == int(d3):
        print(k**2 - int(d3)**2)
    else:
        print(k**2 - d3**2)