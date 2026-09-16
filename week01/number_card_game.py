def solution(n, m):
    result = 0

    for _ in range(n):
        arr = list(map(int, input().split()))
        min_num = min(arr)

        result = max(result, min_num)

    print(result)


n, m = map(int, input().split())
solution(n, m)