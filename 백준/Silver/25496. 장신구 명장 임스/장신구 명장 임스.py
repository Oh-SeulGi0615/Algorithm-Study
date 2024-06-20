p, n = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

cnt = 0
while True:
    if p >= 200 or len(arr) <= 0:
        break

    p += arr.pop()
    cnt += 1

print(cnt)