while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    result = [arr[1]]
    for i in arr[1:]:
        if i != result[-1]:
            result.append(i)

    print(*result, '$')