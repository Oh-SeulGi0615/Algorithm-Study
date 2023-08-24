def solution(name, yearning, photo):
    yearning_dict = {name[i] : yearning[i] for i in range(len(name))}

    answer = [sum([yearning_dict[j] if j in yearning_dict else 0 for j in i]) for i in photo]
    return answer