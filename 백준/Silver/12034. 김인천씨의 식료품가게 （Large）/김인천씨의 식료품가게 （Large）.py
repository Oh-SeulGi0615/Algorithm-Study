import sys
input = sys.stdin.readline

t = int(input())
for x in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))[::-1]

    arr2, arr3 = [], []
    while len(arr) > 0:       
        arr2.append(arr[0])

        idx = arr.index(int(arr2[-1] * 0.75), 0)
        arr3.append(arr[idx])

        arr.remove(arr[idx])
        arr.remove(arr[0])

    arr3 = arr3[::-1]
    print(f'Case #{x}:', end=' ')
    print(*arr3)