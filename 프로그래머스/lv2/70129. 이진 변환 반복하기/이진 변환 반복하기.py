def solution(s):
    change, number0 = 0, 0
    while True:
        if s == '1':
            break
        s_list = list(s)
        number0 += s_list.count('0')
        s = str(bin(s_list.count('1'))[2:])
        change += 1
    return [change, number0]