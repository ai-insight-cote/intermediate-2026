import sys

input = sys.stdin.readline

class Graph:
    """
        어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 
        모든 도로의 거리는 1이다.

        이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
        최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
        또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
    """
    def __init__(self, N: int, X: int):
        self.matrix = [[300_000] * (N+1) for _ in range(N+1)]
        for i in range(N+1):
            self.matrix[i][i] = 0
        self.x = X

    def give_line(self, fro: int, to: int):
        self.matrix[fro][to] = 1

    def no_line(self, fro: int, to: int):
        return self.matrix[fro][to] == 0
        
    def plus_line(self, fro, to1, to2):
        if self.matrix[fro][to2] > self.matrix[fro][to1] + self.matrix[to1][to2] and not self.no_line(fro, to1) and not self.no_line(to1, to2):
            self.matrix[fro][to2] = self.matrix[fro][to1] + self.matrix[to1][to2]

    def search(self, fro, to):
        

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
    def __init__(self, N):
        if not (1<= N <= 1_000_000):
            raise ValueError("N의 값을 제대로 주세요!")
        self.N = N
        self.stack = Stack()
        self.outputs = []

    def input_line(self):

    def main(self):
        for _ in range(self.N):
            self.input_line(input())
    
        sys.stdout.write('\n'.join(self.outputs) + '\n')

if __name__ == "__main__":
    N, M, K, X = map(int, input().strip().split())

    