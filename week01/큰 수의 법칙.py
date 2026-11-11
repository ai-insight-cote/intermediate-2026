# N, M, K 입력 받기
N, M, K = map(int, input().split())

# N개의 자연수 입력
data = list(map(int, input().split()))

data.sort()  # 오름차순정렬

first_num = data[-1]  # 가장 큰 원소 저장
second_num = data[-2]  # 두번째로 큰 원소 저장

i = 0
flag = 0  # 같은 숫자가 연속으로 나오는 횟수 저장
result = 0

while i < M:
    i += 1
    if flag < K:
        result += first_num  # 가장 큰 원소 더함
        flag += 1  # flag + 1
    else:
        result += second_num  # 두번째 큰 원소 더함
        flag = 0  # flag 초기화
    # print(f"{i} {result}")

print(result)
