import sys
input = sys.stdin.readline

n = int(input())

for x in range(1,n+1):
    arr = list(map(int, input().split()))
    arr.sort()

    print(f'Scenario #{x}:')
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('yes')
    else:
        print('no')
    print()