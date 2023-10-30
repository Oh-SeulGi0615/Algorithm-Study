import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n):
    arr = [j for j in range((i*m)+1, ((i+1)*m)+1)]
    print(*arr)