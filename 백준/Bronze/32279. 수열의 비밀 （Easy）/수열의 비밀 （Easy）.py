n = int(input())
p, q, r, s = map(int, input().split())
a_1 = int(input())

arr = [0, a_1]
idx = 2
while idx <= n:
  if idx % 2 == 0:
    arr.append((arr[idx//2] * p) + q)
  else:
    arr.append((arr[(idx-1)//2] * r) + s)
  idx += 1

print(sum(arr))