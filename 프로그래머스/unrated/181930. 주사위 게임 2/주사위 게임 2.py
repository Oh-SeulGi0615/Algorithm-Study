def solution(a, b, c):
    arr = [a, b, c]
    set_ = list(set(arr))
    
    solution = 0
    if len(set_) == 3:
        solution = (a + b + c)
    elif len(set_) == 2:
        solution = (a + b + c) * (a**2 + b**2 + c**2)
    elif len(set_) == 1:
        solution = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        
    return solution