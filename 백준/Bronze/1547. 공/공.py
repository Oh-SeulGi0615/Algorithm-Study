import sys
input = sys.stdin.readline

cup = {1:'ball', 2:0, 3:0}

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    cup[a], cup[b] = cup[b], cup[a]

result = {v:k for k,v in cup.items()}

if 'ball' not in result:
    print(-1)
else:
    print(result['ball'])