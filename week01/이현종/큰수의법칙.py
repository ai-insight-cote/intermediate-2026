# 큰 수의 법칙
# 입력 조건
# - 첫째 줄에 N , M , K 의 자연수가 주어지며, 각 자연수는 공백으로 구분
# - 둘째 줄에 N개의 자연수가 주어짐. 각 자연수는 공백으로 구분, 단 각각의 자연수는 1이상 10000이하의 수로 주어짐
# - 입력으로 주어지는 K는 항상 M보다 작거나 같음.

# 출력 조건
# - 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시           출력 예시
# 5 8 3             46  
# 2 4 5 4 6

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

first = array[n - 1]
second = array[n - 2]
s = int(m / (k + 1))

answer = first * (m - s) + second * s

print(answer)