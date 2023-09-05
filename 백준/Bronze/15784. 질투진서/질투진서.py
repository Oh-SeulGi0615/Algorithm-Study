import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

jinseo = arr[a-1][b-1]

arr2 = [arr[i][b-1] if arr[i][b-1] > jinseo else max(arr[a-1]) if max(arr[a-1]) > jinseo else 0 for i in range(n)]

if max(arr2) > jinseo:
    print('ANGRY')
else:
    print('HAPPY')