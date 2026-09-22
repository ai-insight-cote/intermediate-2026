# N, M 입력 받기
N, M = map(int, input().split())

result = float("-inf")

# N개의 자연수 입력
for i in range(N):
    data = list(map(int, input().split()))

    if result <= min(data):
        result = min(data)
        # print(min(data))  # 디버그용 출력

print(result)
