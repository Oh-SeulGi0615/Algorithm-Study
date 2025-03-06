a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

p, q, r = 0, 0, 0
if min(a/i, b/j, c/k) == a/i:
  p = a - (i * (a/i))
  q = b - (j * (a/i))
  r = c - (k * (a/i))
elif min(a/i, b/j, c/k) == b/j:
  p = a - (i * b/j)
  q = b - (j * b/j)
  r = c - (k * b/j)
else:
  p = a - (i * c/k)
  q = b - (j * c/k)
  r = c - (k * c/k)

print(p, q, r)