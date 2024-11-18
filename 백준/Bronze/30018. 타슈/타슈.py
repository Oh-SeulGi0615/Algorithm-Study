n = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

cnt = 0
for i in range(len(arr_a)):
    if arr_b[i] > arr_a[i]:
        cnt += arr_b[i] - arr_a[i]

print(cnt)