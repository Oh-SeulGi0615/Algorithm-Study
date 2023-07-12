N=int(input())
a=[N]
while a.count(N)<2:
    if N<10:
        N*=11
        a.append(N)
    else:
        N=N%10*10+(N//10+N%10)%10
        a.append(N)
del a[0]
print(a.index(N)+1)