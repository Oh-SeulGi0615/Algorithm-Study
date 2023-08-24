def solution(a, b, n):
    answer = 0
    bottle = n
    while bottle >= a:
        c, d = divmod(bottle, a)
        answer += c * b
        bottle = c * b + d
    return answer