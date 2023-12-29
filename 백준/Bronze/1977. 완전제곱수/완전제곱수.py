import sys
input = sys.stdin.readline

arr = [i ** 2 for i in range(1, 101)]

num1 = int(input())
num2 = int(input())

arr2 = [i for i in range(num1, num2+1) if i in arr]

if len(arr2) > 0:
    print(sum(arr2))
    print(min(arr2))
else:
    print(-1)