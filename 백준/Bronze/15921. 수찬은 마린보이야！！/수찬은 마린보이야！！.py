import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

try:
    avg = sum(arr) / len(arr)
    exv = [i/len(arr) for i in arr]

    if n == 0 or sum(exv) == 0:
        print('divide by zero')
    else:
        print(f'{avg / sum(exv):.2f}')
except:
    print('divide by zero')