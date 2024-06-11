n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

total_t = 0
for shirt in size:
    a, b = divmod(shirt, t)
    if a == 0 and b > 0:
        total_t += 1
    elif a > 0 and b == 0:
        total_t += a
    elif a > 0 and b > 0:
        total_t += a + 1

total_p = n // p

print(total_t)
print(total_p, n - (p * total_p))