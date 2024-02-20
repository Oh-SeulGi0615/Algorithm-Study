def solution(arr):
    from math import gcd
    from functools import reduce
    
    def func(num1, num2):
        multiple = num1 * num2
        gcd_ = gcd(num1, num2)

        result = int(multiple / gcd_)
        return result

    ans = reduce(func, arr)
    return ans