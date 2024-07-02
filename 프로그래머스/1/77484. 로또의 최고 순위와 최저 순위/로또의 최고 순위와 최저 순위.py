def solution(lottos, win_nums):
    from itertools import combinations
    arr = [num for num in lottos if num in win_nums]
    zeros = lottos.count(0)

    high = arr + list(list(combinations([num for num in win_nums if num not in lottos], zeros))[0])
    low = arr
    
    dict_ = {6:1, 5:2, 4:3, 3:4, 2:5}
    answer = []
    if len(high) > 1: answer.append(dict_[len(high)])
    else: answer.append(6)

    if len(low) > 1: answer.append(dict_[len(low)])
    else: answer.append(6)

    return answer