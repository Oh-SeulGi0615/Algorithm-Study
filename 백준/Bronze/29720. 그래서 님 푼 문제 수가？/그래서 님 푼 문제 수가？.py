n, m, k = map(int, input().split())

result = n - (m * k)
print(max(result, 0), max(result + m - 1, 0))