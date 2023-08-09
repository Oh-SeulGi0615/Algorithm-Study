def solution(n):
    if n % 2 == 0:
        answer = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += i ** 2
        return answer
    else:
        answer = 0
        for j in range(1, n+1):
            if j % 2 == 1:
                answer += j
        return answer