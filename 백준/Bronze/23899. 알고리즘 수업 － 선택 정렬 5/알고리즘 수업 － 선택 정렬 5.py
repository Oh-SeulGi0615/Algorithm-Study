import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

state = 0
if arr1 == arr2:
  state = 1

for i in range(n-1, 0, -1):
  sub_arr = arr1[:i+1]
  if sub_arr.index(max(sub_arr)) != i:
    arr1[sub_arr.index(max(sub_arr))], arr1[i] = arr1[i], arr1[sub_arr.index(max(sub_arr))]

  if arr1 == arr2:
    state = 1

print(state)