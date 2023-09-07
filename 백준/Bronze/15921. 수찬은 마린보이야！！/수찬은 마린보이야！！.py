import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print('divide by zero')
else:
    avg = sum(arr) / len(arr)
    exv = [i/len(arr) for i in arr]
    print(f'{avg / sum(exv):.2f}')