# 3-1 거스름돈
def go3_1():
    N = int(input("현금을 입력하세요: "))
    count = 0
    count += N // 500
    N %= 500
    count += N // 100
    N %= 100
    count += N // 50
    N %= 50
    count += N // 10
    print("총 거스름돈의 동전 개수 : {}개".format(count))

# 3-1 거스름돈 *답안
def answer3_1():
    N = int(input("현금을 입력하세요"))
    count = 0

    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += N // coin_types
        N %= coin_types

    print("총 거스름돈의 동전 개수 : {}".format(count))
###################
# 3.2 큰수의법칙    #
###################
def go3_2():
    N, M, K = map(int, input("N, M, K를 입력하세요 : ").split())
    num = map(int, input("숫자들을 입력하세요 :").split())
    count = 0
    answer = 0
    # 첫번째 큰수와 두번째 큰수를 가져온다.
    num1, num2 = sorted(num, reverse=True)[:2]
    for i in range(M):
        if count >= K:
            answer += num2
            count = 0
        else:
            answer += num1
            count += 1
    print(answer)

def answer3_2():
    N, M, K = map(int, input("N, M, K를 입력하세요 : ").split())
    num = map(int, input("숫자들을 입력하세요 :").split())
    count = 0
    answer = 0
    # 첫번째 큰수와 두번째 큰수를 가져온다.
    num1, num2 = sorted(num, reverse=True)[:2]

    count = M // (K + 1) * K
    count += M % (K + 1)

    result = 0
    result += count * num1
    result += (M - count) * num2

    print(answer)
###################
# 3.3 숫자카드게임  #
###################
def go3_3():
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]

    maxNum = 0
    for i in range(N):
        minNum = 100_001
        for j in range(M):
            minNum = min(nums[i][j], minNum)
        maxNum = max(maxNum, minNum)
    print(minNum)


def answer3_3():
    # N, 내을 공백으로 구분하여 입력받기
    n, m = map(int, input().split())
    result = 0
    # 한 줄씩 입력받아 확인
    for i in range(n):
        data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        # '가장 작은 수'들 중에서 가장 큰 수 찾기
    
    result = max(result, min_value)
    print(result) # 최종 답안 출력

###################
# 3.4 1이 될때까지  #
###################
def go3_4():
    n, k = map(int, input().split())
    result = 0
    while n > 1:
        if n % k == 0:
            n //= k 
        else:
            n -= 1
        result += 1
    print(result)

def answer3_4():
    n, k = map(int, input().split())
    result = 0
    while n > 1:
        if n % k == 0:
            n //= k 
            result += 1
        else:
            desc = n % k 
            n -= desc
            result += desc
    print(result)
    

if __name__ == "__main__":
    answer3_4()