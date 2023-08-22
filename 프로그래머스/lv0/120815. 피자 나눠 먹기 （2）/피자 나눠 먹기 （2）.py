def solution(n):
    import math

    gcd = math.gcd(n, 6)
    answer = gcd * int(n / gcd) * int(6 / gcd)
    return int(answer / 6)