import sys
from collections import deque

input = sys.stdin.readline

class Graph:
    """
        어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 
        모든 도로의 거리는 1이다.

        이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
        최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
        또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
    """
    def __init__(self, N: int):
        self.vertex = [[] for _ in range(N+1)]
        self.visited = [False] * (N+1)

    def add_line(self, fro: int, to: int):
        """
        출발지 fro에서 도착지 to로 가는 길을 세운다.
        """
        self.vertex[fro].append(to)

    def show_available(self, fro):
        """
        출발지 fro에서 갈 수 있는 곳을 리스트로 반환한다.
        """
        return self.vertex[fro]

class Buffer:
    """
    - 입력

    첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
    (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 
    두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
    이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

    - 출력

    X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

    이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
    """
    def __init__(self, N, M, K, X):
        if not (2<= N <= 300_000):
            raise ValueError("N의 값을 제대로 주세요!")
        if not (1<= M <= 1_000_000):
            raise ValueError("M의 값을 제대로 주세요!")
        if not (1<= K <= 300_000):
            raise ValueError("K의 값을 제대로 주세요!")
        if not (1<= X <= N):
            raise ValueError("X의 값을 제대로 주세요!")
        self.Graph = Graph(N)
        self.M = M
        self.K = K
        self.X = X
        self.outputs = []

    def input_line(self, input_line: str):
        fro, to = map(int, input_line.split())
        self.Graph.add_line(fro, to)

    def main(self):
        for _ in range(self.M):
            self.input_line(input().strip())

        self.Graph.visited[X] = True
        queue = deque([(X, 0)])
        result = []

        while queue:
            current, length = queue.popleft()
            if length == self.K:
                result.append(current)
                continue
            for visit in self.Graph.show_available(current):
                if self.Graph.visited[visit]:
                    continue
                self.Graph.visited[visit] = True
                queue.append((visit, length+1))

        if result:
            result.sort()
            sys.stdout.write('\n'.join(map(str, result)) + '\n')
        else:
            print(-1)
if __name__ == "__main__":
    N, M, K, X = map(int, input().strip().split())
    buffer = Buffer(N, M, K, X)
    buffer.main()    