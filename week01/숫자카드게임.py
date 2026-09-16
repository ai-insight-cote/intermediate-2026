# 숫자카드게임

# n,m 입력 받기
n,m= map(int,input().split())

# 배열 입력 받기
arr = [list(map(int,input().split())) for _ in range(n)] 

# 하나의 행씩 뽑아서 그 중 가장 작은 수 추출. 그 중에서 가장 큰 수 고르기
answer = max(min(nums) for nums in arr)
print(answer)