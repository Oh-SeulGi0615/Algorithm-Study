mosaic = [[0 for _ in range(100)] for _ in range(100)]

n, m = map(int, input().split())
for _ in range(n):
    arr = list(map(int, input().split()))

    for y in range(arr[1]-1, arr[3]):
        for x in range(arr[0]-1, arr[2]):
            mosaic[y][x] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if mosaic[i][j] > m:
            cnt += 1

print(cnt)