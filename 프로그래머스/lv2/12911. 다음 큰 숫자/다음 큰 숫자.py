def solution(n):
    bin_n = list(str(bin(n)[2:])).count('1')

    cnt = n+1
    while True:
        if list(str(bin(cnt)[2:])).count('1') == list(str(bin(n)[2:])).count('1'):
            break
        cnt += 1
    return cnt