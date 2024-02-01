import sys
input = sys.stdin.readline

dict_ = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 
         5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

n, m = map(int, input().split())
arr = [i for i in range(n, m+1)]

arr_str = []
for i in arr:
    num_list = list(map(lambda x: dict_[x], list(map(int, list(str(i))))))
    string = ' '.join(num_list)
    arr_str.append(string)
arr_str.sort()

arr_num = []
for j in arr_str:
    str_list = j.split()
    str_convert_num = list(map(lambda x: list(dict_.values()).index(x), str_list))

    num = int(''.join(list(map(str, str_convert_num))))
    arr_num.append(num)

arr_num = [arr_num[i:i+10] for i in range(0, len(arr_num), 10)]

for k in arr_num:
    print(*k)