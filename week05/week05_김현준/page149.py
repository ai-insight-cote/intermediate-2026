import collections

def check(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def count_ice_cream(n: int, m: int, graph: list[list[int]]) -> int:
    """음료수 얼려 먹기: 얼음 틀에서 생성되는 총 아이스크림의 개수를 구합니다.

    N x M 크기의 얼음 틀에서 구멍이 뚫려 있는 부분(0)끼리 상, 하, 좌, 우로
    연결되어 있는 경우 하나의 아이스크림으로 간주하여 총 개수를 계산합니다.

    Args:
        n (int): 얼음 틀의 세로 길이 (1 <= n <= 1,000)
        m (int): 얼음 틀의 가로 길이 (1 <= m <= 1,000)
        graph (list[list[int]]): N x M 크기의 얼음 틀 형태.
            구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됨.

    Returns:
        int: 한 번에 만들 수 있는 총 아이스크림의 개수

    Examples:
        >>> ice_tray = [
        ...     [0, 0, 1, 1, 0],
        ...     [0, 0, 0, 1, 1],
        ...     [1, 1, 1, 1, 1],
        ...     [0, 0, 0, 0, 0]
        ... ]
        >>> count_ice_cream(4, 5, ice_tray)
        3
    """

    # (행, 열)(x,y)좌표를 생성하고 (0,0) 좌표부터 인식한다.
    # 이 좌표값이 0이라면 (구멍이뚤려있는부분이라면) 아이스크림 하나로 치고
    # 그 주변을 1로 채운다
    # 주변을 탐색할때, 어떻게? 
    # BFS알고리즘을 통해
    ice_tray = graph
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = 0
    for x in range(n):
        for y in range(m):
            if ice_tray[x][y] == 0:
                result += 1
                deq = collections.deque([(x, y)])
                ice_tray[x][y] = 1
                while deq:
                    cx, cy = deq.popleft()
                    ice_tray[cx][cy] = 1
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if not check(nx, ny, n, m):
                            continue
                        if ice_tray[nx][ny] == 1:
                            continue
                        ice_tray[nx][ny] = 1
                        deq.append((nx,ny))


    return result

if __name__ == "__main__":
    n, m = 15, 14
    ice_tray = [
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    print(count_ice_cream(n, m, ice_tray))  # 예상 출력 결과: 8
    
    

    












