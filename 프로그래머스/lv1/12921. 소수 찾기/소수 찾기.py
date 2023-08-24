def solution(n):
    def check(num):
        for i in range(2, int(num**(1/2)+1)):
            if num % i == 0:
                return False
        return True

    arr = [i for i in range(2, 1000000) if i <= n and check(i) == True]
    return len(arr)