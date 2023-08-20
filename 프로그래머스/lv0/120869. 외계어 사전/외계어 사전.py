def solution(spell, dic):
    dic_dict = {i:0 for i in dic}

    for i in spell:
        for j in dic:
            if dic_dict[j] == 2:
                pass
            else:
                if i in j:
                    dic_dict[j] = 1
                else:
                    dic_dict[j] = 2

    if 1 in dic_dict.values():
        return 1
    else:
        return 2