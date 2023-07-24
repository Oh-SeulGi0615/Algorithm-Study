import sys
input = sys.stdin.readline

while True:
    a, b = map(str, input().split())
    if a == '0' and b == '0':
        break

    arr1 = list(a)[::-1]
    arr2 = list(b)[::-1]

    cnt = 0
    up = 0
    for i in range(min(len(arr1), len(arr2))):
        if up == 0:
            sum_ = int(arr1[i]) + int(arr2[i])
            if sum_ >= 10:
                up = 1
                cnt += 1
        else:
            sum_ = int(arr1[i]) + int(arr2[i]) + up
            if sum_ >= 10:
                cnt += 1

    for j in range(min(len(arr1), len(arr2)), max(len(arr1), len(arr2))):
        if up == 1:
            if len(arr1) > len(arr2):
                if int(arr1[j]) + up >= 10:
                    cnt += 1
            elif len(arr1) < len(arr2):
                if int(arr2[j]) + up >= 10:
                    cnt += 1

    print(cnt)