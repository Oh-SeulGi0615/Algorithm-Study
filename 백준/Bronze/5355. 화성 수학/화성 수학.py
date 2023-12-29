import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(input().split())

    start = float(arr[0])
    for i in arr[1:]:
        if i == '@':
            start *= 3
        elif i == '%':
            start += 5
        elif i == '#':
            start -= 7
    
    print(f'{start:.2f}')