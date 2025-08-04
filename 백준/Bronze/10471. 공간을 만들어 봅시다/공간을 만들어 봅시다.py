w, p = map(int, input().split())
arr = list(map(int, input().split()))

arr.append(0)
arr.append(w)

idx = 0
distance = []
while True:
    if idx >= len(arr):
        break

    for comp in arr:
        result = abs(arr[idx] - comp)
        if result != 0 and result not in distance:
            distance.append(result)

    idx += 1
distance.sort()
print(*distance)