n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x: x[0])

cnt = 1
for i in range(1, n):
  if sum(arr[i-1]) < arr[i][0]:
    cnt += 1

print(cnt)