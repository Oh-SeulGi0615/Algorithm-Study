import sys
input = sys.stdin.readline

check = [True for _ in range(318138)]
check[0], check[1] = False, False

for i in range(2, 318138):
  if check[i] == True:
    for j in range(i*i, len(check), i):
      check[j] = False

nums = [i for i, v in enumerate(check) if v == True]
res = [nums[i] for i, v in enumerate(nums) if check[i+1] == True]

t = int(input())
for _ in range(t):
  n = int(input())
  print(res[n-1])