import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

result = []
for idx_a in range(n):
    arr = []
    for idx_b in range(k):
        mul = 0
        for i in range(m):
            mul += matrix_a[idx_a][i] * matrix_b[i][idx_b]
        arr.append(mul)
    result.append(arr)

for comp in result:
    print(*comp)