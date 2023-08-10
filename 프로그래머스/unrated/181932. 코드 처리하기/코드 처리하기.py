def solution(code):
    ret = []
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
        
        if mode == 0:
            if i % 2 == 0:
                if code[i] != '1':
                    ret.append(code[i])
        else:
            if i % 2 == 1:
                if code[i] != '1':
                    ret.append(code[i])
    
    if len(ret) > 0:
        answer = ''.join(ret)
        return answer
    else:
        return 'EMPTY'