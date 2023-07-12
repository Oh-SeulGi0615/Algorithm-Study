x=int(input())
def f(x):
    ans=[]
    for i in range(1,x+1):
        if i >= 100:
            if i < 1000:
                if (i%10)-(i//10)%10 == (i//10)%10-(i//100)%10:
                    ans.append(i)
                else:
                    pass
            else:
                pass
        else:
            ans.append(i)
    return len(ans)
print(f(x))