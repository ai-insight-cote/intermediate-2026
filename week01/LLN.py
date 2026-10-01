# # 가장 큰 수 파악
# max_num = 0
# for num in arr:
#     max_num = arr[0]
#     if max_num<num:
#         max_num = num
# # 두번째 큰 수 파악
# sec_num = 0
# for num in arr:
#     sec_num = arr[0]
# ##### 반복 #####
# # 가장 큰 수 K번 합
# # 두번째 수로 횟수 초기화
# # 총 M번 덧셈

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[-1]      # 가장 큰 수
second = data[-2]     # 두 번째로 큰 수

result = 0
count = 0

for _ in range(M):
    if count == K:
        result += second
        count = 0
    else:
        result += first
        count += 1

print(result)