import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
go = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    fro, to = map(int, input().split())
    go[fro].append(to)

visited[X] = True
queue = deque([(X, 0)])
result = []
while queue:
    current, length = queue.popleft()
    if length == K:
        result.append(current)
        continue
    for visit in go[current]:
        if visited[visit]:
            continue
        visited[visit] = True
        queue.append((visit, length + 1))

if result:
    result.sort()
    sys.stdout.write('\n'.join(map(str, result)) + '\n')
else:
    print(-1)
