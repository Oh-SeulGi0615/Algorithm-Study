n, m = map(int, input().split())
a = []
for x in range(n):
    a.append(input())

result = []
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if a[k][l] != 'W':
                        cnt1 += 1
                    if a[k][l] != 'B':
                        cnt2 += 1
                else:
                    if a[k][l] != 'B':
                        cnt1 += 1
                    if a[k][l] != 'W':
                        cnt2 += 1
        result.append(min(cnt1, cnt2))
        
print(min(result))