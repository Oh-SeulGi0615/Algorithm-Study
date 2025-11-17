import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

a, b, c = map(int, input().split())

def power(a, n, mod):
  if n == 0:
    return 1
  x = power(a, n//2, mod)

  if n % 2 == 0:
    return (x * x) % mod
  else:
    return (x * x * a) % mod
  
print(power(a, b, c))