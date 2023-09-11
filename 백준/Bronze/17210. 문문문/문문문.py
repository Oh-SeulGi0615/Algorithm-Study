import sys
input = sys.stdin.readline

n = int(input())
a = int(input())

if n < 6:
    if a == 0:
        arr = [0 if i % 2 == 0 else 1 for i in range(n)]
        for i in range(1,len(arr)):
            print(arr[i])
    else:
        arr = [1 if i % 2 == 0 else 0 for i in range(n)]
        for i in range(1,len(arr)):
            print(arr[i])
else:
    print('Love is open door')