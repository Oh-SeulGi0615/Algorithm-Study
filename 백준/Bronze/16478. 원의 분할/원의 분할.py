import sys
input = sys.stdin.readline

p_ab, p_bc, p_cd = map(int, input().split())
result = (p_ab * p_cd) / p_bc

if result == (p_ab * p_cd) // p_bc:
  print(int(result))
else:
  print(round(result, 6))