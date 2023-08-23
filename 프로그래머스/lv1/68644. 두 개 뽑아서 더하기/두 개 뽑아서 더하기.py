def solution(numbers):
    from itertools import combinations

    arr = list(combinations(numbers, 2))

    answer = []; [answer := answer + [sum(i)] for i in arr if sum(i) not in answer]
    answer.sort()
    return answer