def solution(sides):
    sides.sort()

    max_length = sum(sides) - 1
    min_length = max(sides) - min(sides)
    answer = max_length - min_length
    return answer