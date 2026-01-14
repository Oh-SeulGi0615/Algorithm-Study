import sys
input = sys.stdin.readline

n = int(input())
m = input().rstrip()
k = int(input())

if m == 'annyong':
  if k % 2 != 0:
    print(k)
  elif n > k:
    print(k+1)
  elif n == k:
    print(k-1)

elif m == 'induck':
  if k % 2 == 0:
    print(k)
  elif n > k:
    print(k+1)
  elif n == k:
    print(k-1)