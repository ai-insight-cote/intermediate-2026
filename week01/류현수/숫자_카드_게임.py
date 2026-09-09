"""
전역 최댓값을 입력과 동시에 업데이트 하는 방식으로 O(N) 시간 복잡도로 해결할 수 있다.
각 행을 입력 받을 때 마다 최솟값을 구해 전역 최댓값과 비교하여 갱신하면 된다.
"""

answer = float('-inf')
N, M = map(int, input().split())
for _ in range(N):
    row = min(map(int, input().split()))
    answer = max(answer, row)

print(answer)