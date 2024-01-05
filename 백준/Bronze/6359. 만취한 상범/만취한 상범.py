import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    room = {i:1 for i in range(1, n+1)}
    for j in range(1, n+1):
        for k in range(j, n+1, j):
            if room[k] == 1:
                room[k] = 0
            else:
                room[k] = 1
    print(list(room.values()).count(0))