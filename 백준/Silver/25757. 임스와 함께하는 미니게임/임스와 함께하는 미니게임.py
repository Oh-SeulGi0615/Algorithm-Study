import sys

need_player = {
    'Y': 2, 'F': 3, 'O': 4
}

n, g = sys.stdin.readline().split()

already_played = {}
waiting_queue = []
max_queue_length = need_player[g]-1
play_count = 0

for _ in range(int(n)):
    player = sys.stdin.readline().rstrip()

    if player in already_played or player in waiting_queue:
        continue

    waiting_queue.append(player)
    already_played[player] = True
    max_queue_length -= 1

    if max_queue_length == 0:
        waiting_queue = []
        max_queue_length = need_player[g]-1
        play_count += 1

print(play_count)