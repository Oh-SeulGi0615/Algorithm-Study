def solution(k, tangerine):
    dict_ = {}
    for i in tangerine:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1

    dict_ = sorted(dict_.items(), key=lambda x: -x[1])

    box = []
    capacity = k
    for j in dict_:
        if capacity > 0:
            capacity -= j[1]
            box.append(j[0])
        else:
            break
    return len(box)