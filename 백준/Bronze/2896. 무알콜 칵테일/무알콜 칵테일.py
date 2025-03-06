a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

ratio = min(a/i, b/j, c/k)
a -= i * ratio
b -= j * ratio
c -= k * ratio

print(a, b, c)