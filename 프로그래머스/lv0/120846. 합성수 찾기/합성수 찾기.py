def solution(n):
    answer = 0
    while n > 0:
        divisor = [i for i in range(1, n+1) if n % i == 0]
        if len(divisor) >= 3:
            answer += 1
        n -= 1
    return answer