import sys
input = sys.stdin.readline

check = [True] * 100001
check[0], check[1] = False, False

for i in range(2, len(check)):
  if check[i] == True:
    for j in range(i*i, len(check), i):
      check[j] = False

nums = [idx for idx, v in enumerate(check) if v == True]

t = int(input())
for _ in range(t):
  n = int(input())

  if n in nums:
    print(n, 1)
  else:
    arr = {}
    res = n
    cnt = 0
    while True:
      if res == 1:
        break

      if res % nums[cnt] == 0:
        res //= nums[cnt]

        if nums[cnt] not in arr:
          arr[nums[cnt]] = 1
        else:
          arr[nums[cnt]] += 1
      else:
        cnt += 1
    
    for k, v in arr.items():
      print(k, v)