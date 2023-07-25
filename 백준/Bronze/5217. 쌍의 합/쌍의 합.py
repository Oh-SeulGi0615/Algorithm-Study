import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = int(input())

    arr = []
    for x in range(1, a-1):
        for y in range(x+1, a):
            if x + y == a:
                arr.append([x, y])
    
    print(f'Pairs for {a}:', end=' ')
    if len(arr) == 0:
        print()
    elif len(arr) == 1:
        print(*arr[0])
    else:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(*arr[i])
            else:
                print(*arr[i], end=', ')