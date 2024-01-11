import sys
input = sys.stdin.readline

arr = [1, 2, 3]
list_ = list(input().rstrip())

for i in list_:
    if i == 'A':
        arr[0], arr[1] = arr[1], arr[0]
    elif i == 'B':
        arr[1], arr[2] = arr[2], arr[1]
    else:
        arr[0], arr[2] = arr[2], arr[0]

print(arr.index(1) + 1)