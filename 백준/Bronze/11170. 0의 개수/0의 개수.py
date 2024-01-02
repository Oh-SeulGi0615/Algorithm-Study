import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    cnt = 0
    for i in range(a, b+1):
        arr = list(str(i))
        cnt += arr.count('0')
    
    print(cnt)