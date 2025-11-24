import sys
input = sys.stdin.readline

def f(arr=list, num=int):
    arr.append(num)

    arr_2 = list(str(num))
    result = 0
    for i in arr_2:
        result += int(i)**2

    if result in arr:
        return arr
    else:
        return f(arr, result)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    arr_a, arr_b = [], []
    f(arr_a, a)
    f(arr_b, b)

    cnt = 0
    cnt_list = []
    for_break = True
    for i in range(len(arr_a)):
        for j in range(len(arr_b)):
            if arr_a[i] == arr_b[j]:
                cnt += (i+1) + (j+1)
                cnt_list.append(cnt)
                cnt = 0

    if len(cnt_list) > 0:
        print(a, b, min(cnt_list))
    else:
        print(a, b, 0)