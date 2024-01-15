import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

result = ''
sum_ = 0
for idx in range(m):
    dict_ = {'A':0, 'G':0, 'T':0, 'C':0}
    for i in range(len(arr)):
        dict_[arr[i][idx]] += 1

    dict_list = sorted(dict_.items(), key=lambda x: (-x[1], x[0]))
    result += dict_list[0][0]
    sum_ += n - dict_list[0][1]

print(result, sum_, sep='\n')