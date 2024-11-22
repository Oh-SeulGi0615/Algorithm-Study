num = int(input())
arr = [0 for _ in range(num+1)]

def func(num):
  for i in range(2, num+1):
    arr[i] = arr[i-1] + 1
    if i % 3 == 0:
      arr[i] = min(arr[i // 3] + 1, arr[i])
    if i % 2 == 0:
      arr[i] = min(arr[i // 2] + 1, arr[i])
    if i % 3 == 0 and i % 2 == 0:
      arr[i] = min(arr[i // 3] + 1, arr[i // 2] + 1, arr[i])
  return arr[num]

print(func(num))