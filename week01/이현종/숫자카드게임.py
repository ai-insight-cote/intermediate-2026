# 숫자 카드 게임
# 입력 조건
# - 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어짐
# - 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐.
#   각 숫자는 1 이상 10000 이하의 자연수임
  
# 출력 조건
# - 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력함

# 입력 예시 1         출력 예시 1
# 3 3                 2
# 3 1 2
# 4 1 4
# 2 2 2

# 입력 예시 2         출력 예시 2
# 2 4                  3   
# 7 3 1 8
# 3 3 3 4

n, m = map(int, input().split())

answer = 0
for i in range(n):
    card = list(map(int, input().split()))
    min_card = min(card) 
    answer = max(answer, min_card)

print(answer)