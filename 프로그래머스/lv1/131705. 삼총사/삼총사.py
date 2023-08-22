def solution(number):
    from itertools import combinations

    arr = list(combinations(number, 3))

    answer = 0
    for i in arr:
        if sum(i) == 0:
            answer += 1
    return answer