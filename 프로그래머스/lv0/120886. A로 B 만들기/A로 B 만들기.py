def solution(before, after):
    before_list = sorted(list(before))
    after_list = sorted(list(after))

    if before_list == after_list:
        return 1
    else:
        return 0