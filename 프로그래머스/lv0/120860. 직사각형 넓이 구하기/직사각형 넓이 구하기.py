def solution(dots):
    dots.sort()
    y = abs(dots[0][1] - dots[1][1])
    x = abs(dots[0][0] - dots[2][0])
    
    return x * y