def solution(babbling):
    can_speak = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    for i in babbling:
        for j in can_speak:
            if j*2 not in i:
                i = i.replace(j,' ')
        if len(i.strip()) == 0:
            cnt += 1
    return cnt
                