n = int(input())
arr = list(map(int, input().split()))

s, l = 0, 0
for i in arr:
    if i > 0:
        s += 1
        l = max(s, l)
    else:
        s = 0

print(l)