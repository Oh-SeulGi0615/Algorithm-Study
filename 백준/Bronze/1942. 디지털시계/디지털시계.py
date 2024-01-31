import sys
input = sys.stdin.readline

for _ in range(3):
    string1, string2 = map(str, input().split())
    arr1, arr2 = list(map(lambda x: x.split(':'), [string1, string2]))
    a = list(map(int, arr1))
    b = list(map(int, arr2))

    cnt = 0
    while True:
        result = int(''.join(list(map(str, a))))
        if result % 3 == 0:
            cnt += 1

        if a == b:
            break

        a[2] += 1
        if a[2] == 60:
            a[1] += 1
            a[2] = 0
        if a[1] == 60:
            a[0] += 1
            a[1] = 0
        if a[0] == 24:
            a[0] = 0

    print(cnt)