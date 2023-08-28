import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

cnt = [i for i in arr if i > 0]
print(len(cnt))