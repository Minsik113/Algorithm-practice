from collections import deque

n, l, r = map(int, input().split())

# 나라 정보 받기
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 특정위치에서 출발 -> 사이클 끝나면 갱신
def process(x, y, index):
    # (x, y)위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x,y))
    
    # bfs
    q = deque()
    q.append((x, y))
    union[x][y] = index # 연합에 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 안 and 안본 나라
            if 0 <= nx and nx < n and 0 <= ny and ny < n and union[nx][ny] == -1:
                # 옆 나라와 인구차이 비교
                t = abs(graph[nx][ny] - graph[x][y])
                # 조건에 부합하다면
                if l <= t and t <= r: 
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    
    # 연합 국가끼리 인구 재분배한다
    for i, j in united:
        graph[i][j] = summary // count

# 더 이상 인구이동을 할 수 없을 때까지 반복
total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라를 처리하지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1
print(total_count)
                