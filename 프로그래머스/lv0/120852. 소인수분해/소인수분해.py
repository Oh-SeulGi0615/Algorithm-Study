def pn_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(n):
    prime_number = [i for i in range(2, n+1) if pn_check(i) == True]

    answer = []
    for i in prime_number:
        if n % i == 0:
            answer.append(i)
            n = int(n / i)
    return answer