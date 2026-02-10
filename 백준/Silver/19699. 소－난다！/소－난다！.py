import sys
input = sys.stdin.readline

num_list = [True for _ in range(9001)]
num_list[0], num_list[1] = False, False

for i in range(2, 9001):
  if num_list[i] == True:
    for j in range(i*2, 9001, i):
      num_list[j] = False

prime_num = set([idx for idx, value in enumerate(num_list) if value == True])

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

comb = sorted(list(set([i for i in list(map(sum, combinations(arr, m))) if i in prime_num])))

if len(comb) > 0:
  print(*comb)
else:
  print(-1)