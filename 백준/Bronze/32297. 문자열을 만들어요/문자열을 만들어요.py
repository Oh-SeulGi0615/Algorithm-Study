import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

if 'gori' in string:
  print('YES')
else:
  print('NO')