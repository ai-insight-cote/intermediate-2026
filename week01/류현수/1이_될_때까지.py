"""
N = K**a + b로 나타낼 수 있다.
b는 K로 나눈 나머지로 구할 수 있고,
a는 logK(N)의 정수부로 구할 수 있다.
b만큼 1번 연산,
a만큼 2번 연산을 수행하면 된다.
따라서 답은 a+b이다.
시간 복잡도는 O(1)이다.
"""
from math import log
N, K = map(int, input().split())
print(int(log(N, K)) + N % K)