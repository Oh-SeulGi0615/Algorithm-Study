n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort(key=lambda x: x[0])

now_idx = 0
cnt = 0
distance = 10**5
while now_idx < n:
    now_position = line[now_idx][0]
    now_color = line[now_idx][1]

    for idx in range(len(line)):
        if idx == now_idx:
            continue
        else:
            if (line[idx][1] == now_color) and ((max(line[idx][0], now_position) - min(line[idx][0], now_position)) < distance):
                distance = max(line[idx][0], now_position) - min(line[idx][0], now_position)
    
    cnt += distance
    distance = 10**5
    now_idx += 1

print(cnt)