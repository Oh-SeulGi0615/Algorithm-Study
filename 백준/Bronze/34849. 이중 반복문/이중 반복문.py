import sys
input = sys.stdin.readline

n = int(input())

if n ** 2 <= 10**8:
  print('Accepted')
else:
  print('Time limit exceeded')