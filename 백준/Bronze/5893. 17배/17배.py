import sys
input = sys.stdin.readline

n = '0b' + input().rstrip()
s = int(n, 2) * 17
a = format(s, 'b')

print(a)