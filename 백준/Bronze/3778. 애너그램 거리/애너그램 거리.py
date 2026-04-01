import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
for i in range(n):
  a = input().rstrip()
  b = input().rstrip()

  dict_a = Counter(a)
  dict_b = Counter(b)

  dict_c = Counter({i: min(dict_a[i], dict_b[i]) for i in dict_a.keys() & dict_b.keys()})
  res_a = dict_a - dict_c
  res_b = dict_b - dict_c

  res = sum(res_a.values()) + sum(res_b.values())
  print(f'Case #{i+1}: {res}')