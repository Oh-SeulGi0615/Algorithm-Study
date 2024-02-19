def solution(brown, yellow):
    wh = int((brown + 4) / 2)
    wh_list = [(i, wh - i) for i in range(3, wh) if i <= wh - i]
    
    answer = []
    for w, h in wh_list:
        if (w-2) * (h-2) == yellow:
            answer.append(max(w, h))
            answer.append(min(w, h))

    return answer