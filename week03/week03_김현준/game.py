map = [[1,1,1,1],
       [1,0,0,1],
       [1,1,0,1],
       [1,1,1,1]]

def game(x, y, dir):
    """
    입력 조건
    • 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=N,M<=50)
    • 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 
        (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 
        방향 선의 값으로는 다음과 같이 4가지가 존재한다.
        - 0: 북쪽
        -1: 동쪽
        一 2: 남쪽
        一 3: 서쪽
    • 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. 
        N 개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
      맵의 외곽은 항상 바다로 되어 있다.
    - 0: 육지
    一 1: 바다
    • 차음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
    출력 조건 
    • 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
    """
    diff = [(-1, 0), (0,-1), (1,0), (0,1)]
    count = 0
    isFound = True
    while True:
        isFound = False
        for _ in range(4):
            dx = x + diff[dir][0]
            dy = y + diff[dir][1]
            if map[dx][dy] == 0:
                isFound = True
                x = dx
                y = dy
                map[dx][dy] = 2
                count += 1
                break
            dir = (dir - 1) % 4

        if not isFound:
            dir = (dir + 2) % 4
            x = x + diff[dir][0]
            y = y + diff[dir][1]
            if map[x][y] == 1:
                return count

if __name__ == "__main__":
    game(1,1,0)