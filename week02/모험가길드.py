#1
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 
# count = 0 

# for i in data:
#     count += 1 
#     if count >= i:
#         result += 1
#         count = 0

# print(result)

#2
n = int(input())
data = list(map(int, input().split()))
data.sort()

c=0
result=0

while c < n:
    # 현재 위치(c)부터 한 명씩 인원(k)을 늘려가며 그룹 성립 조건을 통과할 때까지 반복
    k = 1
    while c + k <= n and data[c + k - 1] > k:
        k += 1 
        
    # 그룹 결성 조건이 충족되어 최종 인원수(k)가 확정되었다면
    if c + k <= n:
        result += 1
        c += k # 확정된 인원수만큼 훌쩍 인덱스 점프!
    else:
        break