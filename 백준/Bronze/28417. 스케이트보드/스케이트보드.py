n = int(input())

best_rating = 0
for _ in range(n):
    score = list(map(int, input().split()))
    
    run_score = max(score[:2])
    trick_score = sorted(score[2:], key=lambda x: -x)
    rating = run_score + trick_score[0] + trick_score[1]

    if rating > best_rating:
        best_rating = rating

print(best_rating)