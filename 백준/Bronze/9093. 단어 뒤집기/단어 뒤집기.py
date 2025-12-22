import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  string = input().rstrip().split()
  string = list(map(lambda x: x[::-1], string))
  res = ' '.join(string)

  print(res)