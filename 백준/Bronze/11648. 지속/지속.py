import sys
input = sys.stdin.readline

arr = list(input().rstrip())

result = 1
cnt = 0

if len(arr) == 1:
    print(0)
else:
    while len(arr) > 1:
        for i in arr:
            result = result * int(i)
        
        arr = list(str(result))
        result = 1
        cnt += 1

    print(cnt)