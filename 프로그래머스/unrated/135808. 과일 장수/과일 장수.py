def solution(k, m, score):
    score = sorted(score)[::-1]

    answer = 0
    for i in range(m, ((len(score) // m) * m)+1, m):
        answer += score[i-1] * m
    return answer