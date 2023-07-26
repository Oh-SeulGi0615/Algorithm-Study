import sys
input = sys.stdin.readline

w, m, k = map(int, input().split())

team = 0
for i in range(k+1):
    if w-i <= 0 or m-(k-i) <= 0:
        pass
    else:
        wt = w - i
        mt = m - (k-i)
        if team < min(wt//2, mt):
            team = min(wt//2, mt)

print(team)