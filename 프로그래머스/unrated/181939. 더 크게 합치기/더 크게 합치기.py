def solution(a, b):
    answer1 = int(''.join([str(a), str(b)]))
    answer2 = int(''.join([str(b), str(a)]))
    return max(answer1, answer2)