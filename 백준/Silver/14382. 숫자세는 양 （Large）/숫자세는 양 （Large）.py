for i in range(1, int(input())+1):
    cnt = {i:False for i in range(10)}

    n = int(input())
    if n == 2*n == 3*n == 5*n == 7*n:
        print(f'Case #{i}: INSOMNIA')
    else:
        arr = list(map(int, list(str(n))))
        
        k = 1
        while True:
            arr = list(map(int, list(str(n*k))))
            for j in arr:
                cnt[j] = True
            
            if False not in list(cnt.values()):
                print(f'Case #{i}: {n*k}')
                break
            k+=1