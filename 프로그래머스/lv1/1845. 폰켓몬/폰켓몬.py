def solution(nums):
    set_nums = list(set(nums))

    if len(set_nums) >= int(len(nums) / 2):
        return len(set_nums[:int(len(nums) / 2)])
    else:
        return len(set_nums)