def solution(x1, x2, x3, x4):
    def f1(a, b):
        if a == True and b == False or a == False and b == True:
            return False
        elif a == b == True:
            return True
        elif a == b == False:
            return False
    
    def f2(a, b):
        if a == True and b == False or a == False and b == True:
            return True
        elif a == b == True:
            return True
        elif a == b == False:
            return False

    return f1(f2(x1, x2), f2(x3, x4))