# 규칙 찾아보기
# 6 5  m=6 k=2  ->  6 6 5 6 6 5  6//3 = 2
#      m=8 k=2  ->  6 6 5 6 6 5 6 6  8//3 = 2
#      m=9 k=2  ->  6 6 5 6 6 5 6 6 5 

def bigger_sum(n, m, k, arr):  # m = 총 횟수, k=몇번 연속
    arr.sort(reverse=True)
    answer = 0
    answer += arr[0] * (m - m // (k + 1)) + arr[1] * (m // (k + 1))
    return answer

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
print(bigger_sum(n, m, k, arr))