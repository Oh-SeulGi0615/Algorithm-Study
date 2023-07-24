import sys
input = sys.stdin.readline

arr = []
while True:
    n = float(input())
    if int(n) == 999:
        break
    arr.append(n)

for i in range(1,len(arr)):
    sub = arr[i] - arr[i-1]
    print(f'{sub:.2f}')