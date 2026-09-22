# week01	09/16	OT + 그리디 (3장)
# 2. 숫자 카드 게임
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for x in data:
        min_value = min(min_value, x)
    
    result = max(result, min_value)

print(result)