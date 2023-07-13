import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

sec = 0
if a < 0:
    sec += (0-a) * c
    sec += d
    sec += b * e
else:
    sec += (b-a) * e

print(sec)