arr = sorted([list(map(str, input().split())) for _ in range(int(input()))], key=lambda x: int(x[1]))
print(arr[0][0])