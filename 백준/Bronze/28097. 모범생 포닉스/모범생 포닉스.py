import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    a = int(input())

    b, c = divmod(a, 24)
    print(b, c)

else:
    arr = list(map(int, input().split()))
    
    sum = sum(arr) + ((len(arr) - 1) * 8)
    b, c = divmod(sum, 24)
    print(b, c)