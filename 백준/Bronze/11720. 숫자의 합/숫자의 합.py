N=int(input())
a=input()
b=[]
sum=0
for i in range(N):
    b.append(a[i])
for j in range(N):
    b[j]=int(b[j])
    sum+=b[j]
print(sum)