import sys
input = sys.stdin.readline

n = int(input())

arr = []
for x in range(n):
    a, b = map(int, input().split())

    if a > b:
        pass
    else:
        arr.append(b)
    
if len(arr) > 0:
    print(min(arr))
else:
    print(-1)