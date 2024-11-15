t = int(input())

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

arr = [i for i in range(2, 10000) if check(i) == True]

hash_map = {i:[] for i in range(4, 10001, 2)}

for a in range(len(arr)-1):
    for b in range(a, len(arr)):
        if (arr[a] + arr[b]) % 2 == 0 and (arr[a] + arr[b] <= 10000):
            hash_map[arr[a]+arr[b]].append([arr[a], arr[b]])

for _ in range(t):
    n = int(input())
    
    case_ = hash_map[n]
    if len(case_) == 1:
        print(f'{case_[0][0]} {case_[0][1]}')
    else:
        case_.sort(key=lambda x: abs(x[0] - x[1]))
        print(f'{case_[0][0]} {case_[0][1]}')