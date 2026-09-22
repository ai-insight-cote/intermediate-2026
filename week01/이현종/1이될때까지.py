# # 1이 될 때까지
# 입력 조건 
# - 첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어짐.
#   이때 입력으로 주어지는 N은 항상 K보다 크거나 같음
# 출력 조건
# - 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다

# 입력 예시       출력 예시
# 25 5            2


n, k = map(int, input().split())

trial = 0

while n >= k :
    
    if n % k != 0:
        n = n - 1
        trial += 1
    else :
        n = n / k
        trial += 1

while n > 1 :
    n -= 1
    trial += 1

print(trial)