def solution(babbling):
    can_speak = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    for word in babbling:
        compare = ''
        temp = ''
        
        for char in word:
            compare += char
            
            if compare == temp:
                break
            
            if compare in can_speak:
                temp = compare
                compare = ''
        
        if compare == '':
            cnt += 1
    
    return cnt
                