n = int(input())
arr = input().split()
m, k = map(int, input().split())

kiwi = []
for _ in range(m):
    arr2 = list(map(int, input().split()))

    result = []
    for comp in arr2:
        result.append(arr[comp-1])

    if 'P' in result:
        kiwi.append('P')
    else:
        kiwi.append('W')

if 'W' in kiwi:
    print('W')
else:
    print('P')