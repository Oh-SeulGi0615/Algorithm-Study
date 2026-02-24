import sys
input = sys.stdin.readline

n, p = map(int, input().split())

nums, nums_set = [], set()
now = n

nums.append(now)
nums_set.add(now)
while True:
  next_num = (now * n) % p

  if next_num in nums_set:
    idx = nums.index(next_num)
    print(len(nums[idx:]))
    break

  nums.append(next_num)
  nums_set.add(next_num)
  now = next_num