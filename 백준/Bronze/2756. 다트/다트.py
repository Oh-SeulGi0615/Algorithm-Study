import sys
input = sys.stdin.readline

import math

for _ in range(int(input())):
    arr = list(map(float, input().split()))

    p1, p2 = arr[:6], arr[6:]

    total_score = []
    for p in [p1, p2]:
        score = 0
        for i in range(0, len(p1), 2):
            distance = math.sqrt((p[i]**2) + (p[i+1]**2))

            if distance <= 3:
                score += 100
            elif distance <= 6:
                score += 80
            elif distance <= 9:
                score += 60
            elif distance <= 12:
                score += 40
            elif distance <= 15:
                score += 20
        total_score.append(score)

    if total_score[0] > total_score[1]:
        print(f'SCORE: {total_score[0]} to {total_score[1]}, PLAYER 1 WINS.')
    elif total_score[0] < total_score[1]:
        print(f'SCORE: {total_score[0]} to {total_score[1]}, PLAYER 2 WINS.')
    else:
        print(f'SCORE: {total_score[0]} to {total_score[1]}, TIE.')