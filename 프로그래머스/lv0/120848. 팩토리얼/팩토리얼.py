def solution(n):
    import math

    answer = 1
    while True:
        if math.factorial(answer) > n:
            break
        answer += 1
    return answer-1