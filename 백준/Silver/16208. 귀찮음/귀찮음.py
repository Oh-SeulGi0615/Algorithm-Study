n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

result = 0
arr_sum = sum(arr)
while len(arr) > 0:
    result += arr[-1] * (arr_sum - arr[-1])
    arr_sum -= arr[-1]
    arr.pop()

print(result)