# week01	09/16	OT + 그리디 (3장)
# 1. 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  
first = data[-1] 
second = data[-2] 

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first 
result += (m - count) * second  

print(result)

