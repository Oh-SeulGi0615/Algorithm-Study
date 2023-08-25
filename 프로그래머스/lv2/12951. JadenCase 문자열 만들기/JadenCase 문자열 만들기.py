def solution(s):
    s_list = [list(i) for i in s.split(' ')]

    answer = []
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            if j == 0 and s_list[i][j].isalpha() == True:
                s_list[i][j] = s_list[i][j].upper()
            elif j != 0 and s_list[i][j].isalpha() == True:
                s_list[i][j] = s_list[i][j].lower()
        str_ = ''.join(s_list[i])
        answer.append(str_)
    return ' '.join(answer)