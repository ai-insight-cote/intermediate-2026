"""
각 자연 수 중 가장 큰 수를 K번 더하고, 
그 다음으로 큰 수를 한 번 더하는 것을 반복한다.

2개의 큰 수를 구할 때는 정렬이 아닌 선형 탐색을 통해 O(N)으로 구할 수 있다.
이후 최대 합은 일반식을 구하여 O(1)로 구할 수 있다.
최종 시간 복잡도는 O(N)이다.

최대 합 일반식
2번째로 큰 수를 더하는 횟수 = M // (K + 1)
"""

N, M, K = map(int, input().split())
numbers = list(map(int, input().split())) # N개
top1, top2 = float('-inf'), float('-inf')

for n in numbers:
    if n > top2:
        top2 = n
        if top2 > top1:
            top1, top2 = top2, top1

top2_count = M // (K + 1)
result = top1 * (M - top2_count) + top2 * top2_count
print(result)