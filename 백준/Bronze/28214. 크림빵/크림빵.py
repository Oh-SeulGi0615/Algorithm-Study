n, k, p = map(int, input().split())

arr, sub = [], []
for num in list(map(int, input().split())):
    if len(sub) < k:
        sub.append(num)
    else:
        arr.append(sub)
        sub = []
        sub.append(num)
if sub:
    arr.append(sub)

cnt = 0
for sub in arr:
    if sub.count(0) < p:
        cnt += 1

print(cnt)