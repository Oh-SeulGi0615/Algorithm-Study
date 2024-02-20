def solution(participant, completion):
    dict_ = {}
    for i in participant:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
    
    for j in completion:
        dict_[j] -= 1
    
    for k in participant:
        if dict_[k] == 1:
            return k