#숫자 카드 1
n,m=map(int,input().split())
data=list()

for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    result=max(result,min_value)

print(result)

#숫자 카드 2 (min_value for 문으로 찾기)
min_value=10001
for s in data:
    min_value=min(min_value,s)
result=max(result,min_value) #n번 반복
