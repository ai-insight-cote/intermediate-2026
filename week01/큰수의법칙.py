# 큰수의 법칙 1

n,m,k=map(int, input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

#큰수의 법칙 2 (큰수가 더해지는 횟수 구하기)
count= int(m/(k+1))*k #큰수가 더해지는 횟수 (->count = (m // (k + 1)) * k)
count+=m%(k+1)

result=0
result+=(count)*first
result+=(m-count)*second

#큰수의 법칙 3 (second 의 횟수를 구하기)
count=int(m/(k+1))
result=0
result+=count*second
result+=(m-count)*first


