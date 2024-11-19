n, l = map(int, input().split())

best, cnt = 0, 0
for _ in range(n):
    z = input().replace('0', ' ').split()
    
    if len(z) > best:
        best = len(z)
        cnt = 1
    elif len(z) == best:
        cnt += 1

print(best, cnt)