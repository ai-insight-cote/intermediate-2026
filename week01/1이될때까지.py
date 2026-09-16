#1이 될 때까지 1
n,k=map(int,input().split())
result=0
while n!=1:
    if n%k==0:
        n=n//k

    else:
        n-=1
    result+=1

print(result)

#1이 될 때까지 2
while n>=k:
    while n%k!=0:
        n-=1
        result+=1
    n=n//k
    result+=1

while n>1:
    n-=1
    result+=1

#1이 될때까지 3
while n>=k:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k

result+=(n-1)