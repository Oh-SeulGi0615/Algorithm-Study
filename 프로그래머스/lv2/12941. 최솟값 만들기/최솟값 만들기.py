def solution(a,b):
    a = sorted(a)
    b = sorted(b)[::-1]

    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer