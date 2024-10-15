q = int(input())

for _ in range(q):
    s = list(input().rstrip())

    if len(s) < 3:
        print(0)
    else:
        cnt = 0
        for i in range(1, len(s)-1):
            wow = ''.join([s[i-1], s[i], s[i+1]])
            if wow == 'WOW':
                cnt += 1
        print(cnt)