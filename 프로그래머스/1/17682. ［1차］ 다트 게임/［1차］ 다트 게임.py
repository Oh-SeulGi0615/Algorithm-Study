def solution(dart):
    score_list = []

    idx = 0
    while len(dart) > 0:
        if dart[idx] in ['S', 'D', 'T']:
            if idx == len(dart)-1 or dart[idx+1] not in ['*', '#']:
                score_list.append(dart[:idx+1])
                dart = dart[idx+1:]
                idx = 0
            elif dart[idx+1] in ['*', '#']:
                score_list.append(dart[:idx+2])
                dart = dart[idx+2:]
                idx = 0
            else:
                idx += 1
        else:
            idx += 1
            
    dict_ = {'S':1, 'D':2, 'T':3}              
    score = [0, 0, 0]
    for i in range(len(score_list)):
        if score_list[i][-1] not in ['*','#']:
            score[i] = int(score_list[i][:-1]) ** dict_[score_list[i][-1]]
        else:
            if score_list[i][-1] == '*':
                if i == 0:
                    score[i] = (int(score_list[i][:-2]) ** dict_[score_list[i][-2]]) * 2
                else:
                    score[i] = (int(score_list[i][:-2]) ** dict_[score_list[i][-2]]) * 2
                    score[i-1] = score[i-1] * 2
            if score_list[i][-1] == '#':
                score[i] = (int(score_list[i][:-2]) ** dict_[score_list[i][-2]]) * -1
    answer = sum(score)
    return answer