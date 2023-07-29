import sys
input = sys.stdin.readline

for x in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    arr.sort()

    print(f'Case #{x}:', end=' ')
    if arr[0] + arr[1] <= arr[2]:
        print('invalid!')
    else:
        if arr[0] == arr[1] == arr[2]:
            print('equilateral')
        elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
            print('isosceles')
        else:
            print('scalene')