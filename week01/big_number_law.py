def solution(n, m, k, nArr):
    arr = list(map(int, nArr.split()))
    arr.sort(reverse=True)

    first = arr[0]
    second = arr[1]

    cycle = k + 1
    count = (m // cycle) * k + min(m % cycle, k)

    result = first * count + second * (m - count)

    print(result)

solution(5, 8, 3, "2 4 5 4 6")