import sys
input = sys.stdin.readline
import math

n = int(input())

u = round(n * n * math.pi, 6)
t = 2 * n * n

print(f'{u:.6f}')
print(f'{t:.6f}')