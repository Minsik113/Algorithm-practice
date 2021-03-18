n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = [] # 방향 회전 정보

# 맵정보 - 사과를 1로 표시
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = map(str, input().split())
    info.append((int(x), c))
# 처음 오른쪽을 보고있으므로 (동남서북)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 맵이 존재하는 위치 2
    direction = 0 # 시작이 동쪽
    time = 0 # 시작한 뒤의 초
    index = 0 # 다음에 회전할 정보
    q = [(x,y)]
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 범위안에 있고, 뱀 안만난다면
        if nx > 0 and ny > 0 and nx <= n and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 그대로
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 몸통과 부딪히면 끝
        else:
            time += 1
            break
        x,y = nx, ny # 다음 위치로 이동
        time += 1

        if index < l and time == info[index][0]: # 회전할 시간
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())

