from itertools import combinations

n = int(input())

cnt = []
for i in range(n):
  arr = list(map(int, input().split()))
  comb = sum(sorted(list(combinations(arr, 3)), key=lambda x: -(sum(x) % 10))[0]) % 10
  cnt.append(comb)

result = [i for i, ele in enumerate(cnt) if ele == max(cnt)]
print(max(result)+1)