n = int(input())

score = {i:0 for i in range(1, n+1)}
for _ in range(int(n*(n-1)/2)):
    a, b, c, d = map(int, input().split())
    if c > d:
        score[a] += 3
    elif c < d:
        score[b] += 3
    elif c == d:
        score[a] += 1
        score[b] += 1

rank = sorted(list(score.values()))[::-1]
for i in range(1, n+1):
    print(rank.index(score[i]) + 1)