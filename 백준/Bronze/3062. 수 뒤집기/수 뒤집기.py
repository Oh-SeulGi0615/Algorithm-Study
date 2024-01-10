import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int, list(input().rstrip())))
    arr_ = arr[::-1]

    num1 = int(''.join(list(map(str, arr))))
    num2 = int(''.join(list(map(str, arr_))))
    num = num1 + num2

    if list(str(num)) == list(str(num))[::-1]:
        print('YES')
    else:
        print('NO')