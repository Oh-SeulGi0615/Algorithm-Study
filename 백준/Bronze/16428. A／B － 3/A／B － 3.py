a, b = map(int, input().split())

div = 0
mod = 0

if a > 0 and b > 0:
    div = a // b
    mod = a % b
elif a < 0 and b > 0:
    div = a // b
    mod = a % b
elif a > 0 and b < 0:
    div = -1 * (abs(a) // abs(b))
    mod = abs(a) % abs(b)
elif a < 0 and b < 0:
    div = -1 * (a // abs(b))
    mod = a - (b * div)

print(div)
print(mod)