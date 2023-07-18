import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    a = arr[1:]

    sum = 1
    for i in range(len(a)):
        if i % 2 == 0:
            sum = sum * a[i]
        elif i % 2 == 1:
            sum -= a[i]
    
    print(sum)