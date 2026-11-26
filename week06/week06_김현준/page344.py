import sys
from collections import deque

class Matrix:
    def __init__(self, N, K):
        self.matrix = [[0] * K for _ in range(N)]

    