# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()         # 소트 까먹고 처음에 포문 생각함
first = data[-1]    # 아 맞다 리스트 -1이 맨뒤값이지
second = data[-2]
count = (m // (k + 1)) * k + (m % (k + 1))
result = (count * first) + ((m - count) * second)
print(result)


# 숫자 카드
n, m = map(int, input().split())
min_list = []
for _ in range(n):      # 민 맥스 쓰면 된다니 싫다.
    row = list(map(int, input().split()))
    row.sort()                
    min_list.append(row[0])   
min_list.sort(reverse=True)   
print(min_list[0])            


# 1이 될 때까지
n, k = map(int, input().split())
count = 0
while True:
    remainder = n % k
    count += remainder
    n -= remainder
    if n < k:   # 내가 로직에서 빼먹은 부분.
        break
    n //= k
    count += 1
count += (n - 1)
print(count)