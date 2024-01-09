import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    x, y = divmod(m, 10)

    arr = []
    if y == 0:
        for _ in range(x):
            arr2 = list(map(int, input().split()))
            arr.extend(arr2)
    else:
        for _ in range(x+1):
            arr2 = list(map(int, input().split()))
            arr.extend(arr2)

    result, result2 = [], []
    for i in range(len(arr)):
        result.append(arr[i])

        if len(result) % 2 != 0:
            result.sort()
            result2.append(result[int(len(result) / 2)])

    result3 = [result2[i*10 : (i+1)*10] for i in range((len(result2) + 10 - 1) // 10)]
    
    print(len(result2))
    for j in result3:
        print(*j)