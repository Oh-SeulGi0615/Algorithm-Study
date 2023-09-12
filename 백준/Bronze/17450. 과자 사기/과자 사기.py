import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]

if arr[0][0] < 500:
    s = arr[0][1] / arr[0][0]
else:
    s = arr[0][1] / (arr[0][0] - 50)

if arr[1][0] < 500:
    n = arr[1][1] / arr[1][0]
else:
    n = arr[1][1] / (arr[1][0] - 50)

if arr[2][0] < 500:
    u = arr[2][1] / arr[2][0]
else:
    u = arr[2][1] / (arr[2][0] - 50)

if max(s, n, u) == s:
    print('S')
elif max(s, n, u) == n:
    print('N')
else:
    print('U')