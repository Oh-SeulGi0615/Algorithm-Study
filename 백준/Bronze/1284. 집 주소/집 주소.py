import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    arr = list(str(n))

    sum = 2 + (len(arr) - 1)
    for i in arr:
        if i == '0':
            sum += 4
        elif i == '1':
            sum += 2
        else:
            sum += 3
    
    print(sum)