def solution(nums):
    def check(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    from itertools import combinations

    arr = list(combinations(nums, 3))

    answer = 0
    for i in arr:
        if check(sum(i)) == True:
            answer += 1
    return answer